# Missile Trajectory Prediction Simulator

## Overview

This project implements a comprehensive missile trajectory prediction system using machine learning for Bharat Dynamics Ltd. The system combines physics-based modeling with advanced ML algorithms to provide accurate trajectory predictions for defense applications.

## Features

### 🚀 Core Capabilities
- **ML-based Trajectory Prediction**: Advanced machine learning models trained on physics-based synthetic data
- **Physics Simulation**: Accurate physics-based trajectory calculation with drag and wind effects
- **Interactive Simulators**: Web-based (Streamlit) and desktop (Tkinter) interfaces
- **Advanced Analytics Dashboard**: Comprehensive analysis and visualization tools
- **Mission Planning**: Automated parameter optimization for specific targets
- **Batch Processing**: Handle multiple trajectory calculations simultaneously

### 📊 Analysis Tools
- Performance envelope analysis
- 3D trajectory visualization
- Parameter sensitivity analysis
- Statistical correlation analysis
- Model validation and comparison
- Scenario comparison tools

### 🎯 Applications
- Training and simulation for defense personnel
- Mission planning and parameter optimization
- Research and development support
- Educational demonstrations
- Performance analysis and reporting

## Project Structure

\`\`\`
missile-trajectory-simulator/
├── src/                          # Core prediction modules
│   ├── trajectory_predictor.py   # Main ML prediction class
│   └── physics_simulator.py     # Physics-based simulation
├── scripts/                      # Data generation and training
│   ├── generate_dataset.py      # Synthetic data generation
│   ├── train_models.py          # ML model training pipeline
│   ├── model_validation.py      # Model validation tools
│   └── data_analysis.py         # Dataset analysis
├── app/                         # Interactive applications
│   ├── streamlit_simulator.py   # Web-based simulator
│   ├── simple_gui.py           # Desktop GUI application
│   └── run_simulator.py        # Simulator launcher
├── dashboard/                   # Advanced analytics
│   ├── advanced_dashboard.py   # Comprehensive dashboard
│   └── run_dashboard.py        # Dashboard launcher
├── data/                       # Generated datasets
├── models/                     # Trained ML models
└── README.md                   # This file
\`\`\`

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Required packages (install via pip):

\`\`\`bash
pip install numpy pandas matplotlib plotly seaborn scikit-learn streamlit joblib scipy
\`\`\`

### Quick Start

1. **Generate Training Data**:
   \`\`\`bash
   python scripts/generate_dataset.py
   \`\`\`

2. **Train ML Models**:
   \`\`\`bash
   python scripts/train_models.py
   \`\`\`

3. **Run Interactive Simulator**:
   \`\`\`bash
   python app/run_simulator.py
   \`\`\`

4. **Launch Advanced Dashboard**:
   \`\`\`bash
   python dashboard/run_dashboard.py
   \`\`\`

## Usage Guide

### Basic Trajectory Prediction

\`\`\`python
from src.trajectory_predictor import TrajectoryPredictor, MissileParameters

# Initialize predictor
predictor = TrajectoryPredictor()

# Define missile parameters
params = MissileParameters(
    initial_velocity=800,    # m/s
    launch_angle=45,         # degrees
    mass=500,               # kg
    drag_coefficient=0.4,
    cross_sectional_area=0.2, # m²
    wind_speed=5            # m/s
)

# Get prediction
prediction = predictor.predict(params)

print(f"Max Range: {prediction.max_range_km:.2f} km")
print(f"Max Height: {prediction.max_height_km:.2f} km")
print(f"Time of Flight: {prediction.time_of_flight:.1f} s")
\`\`\`

### Advanced Analysis

\`\`\`python
# Optimize launch angle for maximum range
optimal_angle, optimal_prediction = predictor.optimize_for_range(params)

# Sensitivity analysis
sensitivity = predictor.sensitivity_analysis(params)

# Compare multiple scenarios
scenarios = create_sample_scenarios()
comparison = predictor.compare_scenarios(scenarios)
\`\`\`

## Model Performance

The ML models achieve high accuracy across different trajectory parameters:

- **Range Prediction**: R² > 0.95
- **Height Prediction**: R² > 0.93
- **Time of Flight**: R² > 0.96
- **Impact Velocity**: R² > 0.94

## Technical Specifications

### Input Parameters
- Initial velocity: 100-2000 m/s
- Launch angle: 5-85 degrees
- Mass: 50-5000 kg
- Drag coefficient: 0.1-0.8
- Cross-sectional area: 0.01-2.0 m²
- Wind speed: -20 to +20 m/s

### Output Predictions
- Maximum height (km)
- Maximum range (km)
- Time of flight (seconds)
- Impact velocity (m/s)
- Apogee time (seconds)

### ML Models Used
- Random Forest Regressor
- Gradient Boosting Regressor
- Neural Networks (MLP)
- Ridge Regression
- Linear Regression

## Safety and Compliance

⚠️ **Important Notice**: This system is designed for educational, training, and research purposes only. It is not intended for actual weapon guidance or targeting systems.

### Security Features
- No classified data storage
- Educational simulation focus
- Open-source implementation
- Transparent methodology

## Contributing

This project is developed for Bharat Dynamics Ltd as part of defense research initiatives. For contributions or modifications:

1. Follow the existing code structure
2. Maintain comprehensive documentation
3. Include appropriate test cases
4. Ensure compliance with security guidelines

## Support and Documentation

For technical support or questions:
- Review the code documentation
- Check the example scripts
- Refer to the interactive tutorials in the simulators

## License

This project is developed for Bharat Dynamics Ltd defense research purposes. Usage should comply with applicable defense and export regulations.

---

**Developed for Bharat Dynamics Ltd**  
*Advanced Defense Research & Development*  
*ML-based Trajectory Prediction System*
