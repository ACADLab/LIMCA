import os
import sys
import shutil
import subprocess
import re
from pathlib import Path
from itertools import product

# Configuration parameters
TECH_NODES = [7e-9, 9e-9, 10e-9, 14e-9, 16e-9, 20e-9]
XBAR_SIZES = [(16, 16)]

# Fixed firstimage value - change this to your desired starting image
FIXED_FIRSTIMAGE = 1000

# Device configurations
DEVICES = {
    'MRAM': {'rlow': 8.5e3, 'rhigh': 25.5e3},
    'RRAM': {'rlow': 2.5e3, 'rhigh': 100e3},
    'CBRAM': {'rlow': 10e3, 'rhigh': 1e6},
    'PCM': {'rlow': 78e3, 'rhigh': 202e3}
}

# Cell configurations
CELL_TYPES = {
    '1T1R': {'L_factor': 15, 'W_factor': 12},
    '2T1R': {'L_factor': 23, 'W_factor': 12},
    '1TG1R': {'L_factor': 48, 'W_factor': 12}
}

def create_variation_name(xbar_size, tech_node, device_type, cell_type):
    """Create a standardized name for the variation"""
    tech_nm = int(tech_node * 1e9)
    return f"{xbar_size[0]}x{xbar_size[1]}_{tech_nm}nm_{device_type}_{cell_type}_first{FIXED_FIRSTIMAGE}"

def modify_code(template_code, config):
    """Modify the code template with new parameters and add path handling"""
    # Get the absolute path of the current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add path handling code at the start
    path_setup = f"""import os
import sys

# Add parent directory to Python path
base_dir = '{base_dir}'
sys.path.append(base_dir)

# Set working directory to base directory for correct file access
os.chdir(base_dir)
"""
    
    modified_code = path_setup + template_code
    
    # Extract parameters from config
    xbar_size = config['xbar_size']
    tech_node = config['tech_node']
    device = config['device']
    cell = config['cell']
    
    # Create a dictionary of replacements - using FIXED_FIRSTIMAGE instead of random
    replacements = [
        (r'xbar=\[\d+,\d+\]', f"xbar=[{xbar_size[0]},{xbar_size[1]}]"),
        (r'tech_node=\d+(?:\.\d+)?e-\d+', f"tech_node={tech_node}"),
        (r'rlow=\d+(?:\.\d+)?e?\d*', f"rlow={DEVICES[device]['rlow']}"),
        (r'rhigh=\d+(?:\.\d+)?e?\d*', f"rhigh={DEVICES[device]['rhigh']}"),
        (r'L=\d+\*tech_node', f"L={CELL_TYPES[cell]['L_factor']}*tech_node"),
        (r'W=\d+\*tech_node', f"W={CELL_TYPES[cell]['W_factor']}*tech_node"),
        (r'firstimage=\d+', f"firstimage={FIXED_FIRSTIMAGE}")  # Fixed value instead of random
    ]
    
    for old, new in replacements:
        modified_code = re.sub(old, new, modified_code)
    
    return modified_code

def extract_results(output):
    """Extract relevant results from the command output"""
    results = {}
    patterns = {
        'power_consumption': r'Power consumption = ([\d.]+)',
        'total_area': r'Total area = ([\d.]+)',
        'error_rate': r'error rate = ([\d.]+)',
        'accuracy': r'accuracy = ([\d.]+)%',
        'avg_power': r'average total power = ([\d.]+)',
        'execution_time': r'Program Execution Time = (\d+) hours (\d+) minutes (\d+) seconds'
    }
    
    print("\nExtracting results from output:")
    
    for key, pattern in patterns.items():
        match = re.search(pattern, output)
        if match:
            results[key] = match.group(1)
            print(f"Found {key}: {match.group(1)}")
        else:
            print(f"Warning: Could not find pattern for {key}")
            results[key] = "N/A"
    
    return results

def run_variations():
    # Get absolute paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    variations_dir = os.path.join(base_dir, '16_norand_cb')
    
    # Create variations directory if it doesn't exist
    os.makedirs(variations_dir, exist_ok=True)
    
    # Read the template code
    with open('testIMAC.py', 'r') as f:
        template_code = f.read()
    
    # Create a summary file for all results
    summary_file = os.path.join(variations_dir, 'all_results_summary.csv')
    with open(summary_file, 'w') as f:
        f.write("Configuration,Power Consumption,Total Area,Error Rate,Accuracy,Average Power,Execution Time\n")
    
    # Generate all possible combinations
    combinations = product(
        XBAR_SIZES,
        TECH_NODES,
        DEVICES.keys(),
        CELL_TYPES.keys()
    )
    
    # Process each combination
    for xbar_size, tech_node, device_type, cell_type in combinations:
        config = {
            'xbar_size': xbar_size,
            'tech_node': tech_node,
            'device': device_type,
            'cell': cell_type
        }
        
        # Create variation name and directory
        var_name = create_variation_name(xbar_size, tech_node, device_type, cell_type)
        var_dir = os.path.join(variations_dir, var_name)
        os.makedirs(var_dir, exist_ok=True)
        
        # Create modified code file
        modified_code = modify_code(template_code, config)
        code_file = os.path.join(var_dir, f'{var_name}.py')
        with open(code_file, 'w') as f:
            f.write(modified_code)
        
        # Run the simulation from the base directory
        try:
            print(f"\nRunning variation: {var_name}")
            
            # Execute the Python script
            process = subprocess.Popen(
                ['python3', code_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                cwd=base_dir  # Run from base directory
            )
            
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                raise Exception(f"Script failed with error: {stderr}")
            
            # Save the complete output
            output_file = os.path.join(var_dir, 'simulation_output.txt')
            with open(output_file, 'w') as f:
                f.write(stdout)
                if stderr:
                    f.write("\n\nSTDERR:\n")
                    f.write(stderr)
            
            # Extract and save results
            results = extract_results(stdout)
            
            # Save individual results
            summary_file = os.path.join(var_dir, 'results_summary.txt')
            with open(summary_file, 'w') as f:
                for key, value in results.items():
                    f.write(f"{key}: {value}\n")
            
            # Append to master summary
            with open(os.path.join(variations_dir, 'all_results_summary.csv'), 'a') as f:
                f.write(f"{var_name},{results.get('power_consumption', 'N/A')}," + 
                       f"{results.get('total_area', 'N/A')},{results.get('error_rate', 'N/A')}," +
                       f"{results.get('accuracy', 'N/A')},{results.get('avg_power', 'N/A')}," +
                       f"{results.get('execution_time', 'N/A')}\n")
            
            print(f"Completed variation: {var_name}")
            
        except Exception as e:
            print(f"Error running variation {var_name}: {str(e)}")
            with open(os.path.join(variations_dir, 'error_log.txt'), 'a') as f:
                f.write(f"Error in {var_name}: {str(e)}\n")

if __name__ == "__main__":
    print("Starting variation generator...")
    print(f"Using fixed firstimage value: {FIXED_FIRSTIMAGE}")
    total_configs = len(XBAR_SIZES) * len(TECH_NODES) * len(DEVICES) * len(CELL_TYPES)
    print(f"Total configurations to run: {total_configs}")
    run_variations()
    print("\nAll variations completed!")