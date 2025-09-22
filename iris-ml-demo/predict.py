import sys
import joblib
from sklearn.datasets import load_iris

def main():
    if len(sys.argv) != 5:
        print("Usage: python predict.py sepal_length sepal_width petal_length petal_width")
        sys.exit(1)

    # Parse input features
    sample = [float(x) for x in sys.argv[1:]]
    sample = [sample]  # model expects 2D array

    # Load model
    clf = joblib.load("model.joblib")
    iris = load_iris()

    # Predict
    prediction = clf.predict(sample)[0]
    class_name = iris.target_names[prediction]
    print(f"🌸 Predicted class: {class_name}")

if __name__ == "__main__":
    main()
