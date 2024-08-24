This repository contains the results of an A/B testing analysis where various machine learning models, including those from H2O AutoML and XGBoost, were evaluated for predictive accuracy. The H2O AutoML-selected Deep Learning model outperformed others, achieving an RMSE of 19.08 and MAE of 16.54, with positive R-squared values. In contrast, the XGBoost model, using a gblinear booster, showed suboptimal performance with an RMSE of 29.94 and a negative R-squared, indicating the need for further tuning and optimization.

Suggested Improvements:
Switch to gbtree Booster: For XGBoost, consider using the gbtree booster instead of gblinear to capture non-linear relationships in the data.
Hyperparameter Tuning: Perform grid search or Bayesian optimization to fine-tune model parameters for better performance.
Feature Engineering: Explore additional feature engineering techniques to improve model input.
Cross-Validation: Implement more robust cross-validation strategies to ensure model generalization.
Model Stacking: Experiment with model stacking or ensemble methods to combine the strengths of different models.
