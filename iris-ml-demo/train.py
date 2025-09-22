from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

def main():
    # Load the iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Train a Decision Tree Classifier
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Save the trained model to a file
    joblib.dump(clf, 'model.joblib')
    print("Model trained and saved as 'iris_model.joblib'")

if __name__ == "__main__":
    main()
