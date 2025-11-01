#!/usr/bin/env python3
"""
Complete Missile Trajectory Prediction System Launcher
Bharat Dynamics Ltd - Defense Research Project
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def print_header():
    """Print system header."""
    print("=" * 80)
    print("🚀 MISSILE TRAJECTORY PREDICTION SIMULATOR")
    print("=" * 80)
    print("Bharat Dynamics Ltd - Defense Research & Development")
    print("Advanced ML-based Trajectory Prediction System")
    print("=" * 80)
    print()

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        'numpy', 'pandas', 'matplotlib', 'plotly', 'seaborn',
        'scikit-learn', 'streamlit', 'joblib', 'scipy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   • {package}")
        print("\nInstall missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ All required packages are installed")
    return True

def setup_directories():
    """Create necessary directories."""
    directories = ['data', 'models', 'scripts', 'src', 'app', 'dashboard']
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    
    print("✅ Directory structure verified")

def run_data_generation():
    """Run data generation script."""
    print("\n📊 STEP 1: Generating Synthetic Training Data")
    print("-" * 50)
    
    try:
        result = subprocess.run([sys.executable, 'scripts/generate_dataset.py'], 
                              capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ Training data generated successfully")
            return True
        else:
            print(f"❌ Data generation failed: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Data generation timed out")
        return False
    except Exception as e:
        print(f"❌ Error during data generation: {e}")
        return False

def run_model_training():
    """Run model training script."""
    print("\n🤖 STEP 2: Training Machine Learning Models")
    print("-" * 50)
    
    try:
        result = subprocess.run([sys.executable, 'scripts/train_models.py'], 
                              capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print("✅ ML models trained successfully")
            return True
        else:
            print(f"❌ Model training failed: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Model training timed out")
        return False
    except Exception as e:
        print(f"❌ Error during model training: {e}")
        return False

def run_model_validation():
    """Run model validation."""
    print("\n🔬 STEP 3: Validating Model Performance")
    print("-" * 50)
    
    try:
        result = subprocess.run([sys.executable, 'scripts/model_validation.py'], 
                              capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print("✅ Model validation completed")
            return True
        else:
            print(f"❌ Model validation failed: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Model validation timed out")
        return False
    except Exception as e:
        print(f"❌ Error during model validation: {e}")
        return False

def launch_applications():
    """Launch the applications."""
    print("\n🚀 STEP 4: Launching Applications")
    print("-" * 50)
    
    print("Available applications:")
    print("1. Interactive Web Simulator (Streamlit)")
    print("2. Advanced Analytics Dashboard")
    print("3. Desktop GUI Application")
    print("4. All Applications")
    print("5. Skip application launch")
    
    choice = input("\nSelect application to launch (1-5): ").strip()
    
    if choice == '1':
        launch_web_simulator()
    elif choice == '2':
        launch_dashboard()
    elif choice == '3':
        launch_desktop_gui()
    elif choice == '4':
        launch_all_applications()
    elif choice == '5':
        print("Skipping application launch")
    else:
        print("Invalid choice, skipping application launch")

def launch_web_simulator():
    """Launch the web-based simulator."""
    print("🌐 Launching Web Simulator...")
    try:
        subprocess.Popen([sys.executable, 'app/run_simulator.py'])
        print("✅ Web simulator started at http://localhost:8501")
    except Exception as e:
        print(f"❌ Failed to launch web simulator: {e}")

def launch_dashboard():
    """Launch the analytics dashboard."""
    print("📊 Launching Analytics Dashboard...")
    try:
        subprocess.Popen([sys.executable, 'dashboard/run_dashboard.py'])
        print("✅ Analytics dashboard started at http://localhost:8502")
    except Exception as e:
        print(f"❌ Failed to launch dashboard: {e}")

def launch_desktop_gui():
    """Launch the desktop GUI."""
    print("🖥️ Launching Desktop GUI...")
    try:
        subprocess.Popen([sys.executable, 'app/simple_gui.py'])
        print("✅ Desktop GUI launched")
    except Exception as e:
        print(f"❌ Failed to launch desktop GUI: {e}")

def launch_all_applications():
    """Launch all applications."""
    launch_web_simulator()
    time.sleep(2)
    launch_dashboard()
    time.sleep(2)
    launch_desktop_gui()

def main():
    """Main system launcher."""
    print_header()
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Setup directories
    setup_directories()
    
    # Check if models already exist
    models_exist = Path('models/model_metadata.joblib').exists()
    data_exists = Path('data/missile_trajectory_dataset.csv').exists()
    
    if models_exist and data_exists:
        print("✅ Existing models and data found")
        skip_training = input("Skip data generation and training? (y/n): ").lower().strip() == 'y'
    else:
        skip_training = False
    
    if not skip_training:
        # Step 1: Generate data
        if not run_data_generation():
            print("❌ System setup failed at data generation step")
            return
        
        # Step 2: Train models
        if not run_model_training():
            print("❌ System setup failed at model training step")
            return
        
        # Step 3: Validate models
        if not run_model_validation():
            print("⚠️ Model validation failed, but continuing...")
    
    # Step 4: Launch applications
    launch_applications()
    
    print("\n" + "=" * 80)
    print("🎉 MISSILE TRAJECTORY PREDICTION SYSTEM READY")
    print("=" * 80)
    print("System Components:")
    print("• ✅ Synthetic Data Generator")
    print("• ✅ ML Training Pipeline")
    print("• ✅ Trajectory Predictor")
    print("• ✅ Physics Simulator")
    print("• ✅ Interactive Web Interface")
    print("• ✅ Advanced Analytics Dashboard")
    print("• ✅ Desktop GUI Application")
    print()
    print("🔗 Access Points:")
    print("• Web Simulator: http://localhost:8501")
    print("• Analytics Dashboard: http://localhost:8502")
    print("• Desktop GUI: Launched separately")
    print()
    print("📚 Documentation: README.md")
    print("🛠️ Technical Support: Check code documentation")
    print("=" * 80)

if __name__ == "__main__":
    main()
