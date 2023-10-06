import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def dump_model():
    iris = load_iris(as_frame=True)
    X = iris.data  # Özellikler
    y = iris.target  # Hedef sınıflar

    # Verileri eğitim ve test setlerine bölelim
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Modeli oluşturalım ve eğitelim
    model = SVC(kernel="linear")  # SVM modeli
    model.fit(X_train, y_train)

    # Modelin performansını test edelim
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Test verisi doğruluk oranı: {accuracy}")

    joblib.dump(model, "model.pkl")

    return model


if __name__ == "__main__":
    dump_model()
