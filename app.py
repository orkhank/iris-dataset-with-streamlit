import joblib
import pandas as pd
import streamlit as st


@st.cache_data
def get_prediction(sepal_length, sepal_width, petal_length, petal_width):
    target_names = ["setosa", "versicolor", "virginica"]

    # Unpickle classifier
    try:
        model = joblib.load("model.pkl")
    except FileNotFoundError:
        from model import dump_model

        with st.spinner("Generating model..."):
            model = dump_model()

    # Store inputs into dataframe
    X = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ],
    )

    # Get prediction
    prediction = model.predict(X)[0]

    # Output prediction
    return target_names[prediction]


def show_image(iris):
    image_urls = {
        "setosa": r"https://upload.wikimedia.org/wikipedia/commons/8/85/Iris_setosa01.jpg",
        "versicolor": r"https://upload.wikimedia.org/wikipedia/commons/d/db/Iris_versicolor_4.jpg",
        "virginica": r"https://upload.wikimedia.org/wikipedia/commons/d/d4/Iris_virginica_%28Virginia_iris%29_%28Newark%2C_Ohio%2C_USA%29_8_%2827808217065%29.jpg",
    }

    st.image(image_urls[iris])


if __name__ == "__main__":
    # Title
    st.header("Streamlit Machine Learning App - Iris Dataset")

    with st.sidebar:
        # Input Sliders
        sepal_length = st.slider("Enter Sepal Length (cm)", 4.0, 8.0, step=0.1)
        sepal_width = st.slider("Enter Sepal Width (cm)", 2.0, 5.0, step=0.1)
        petal_length = st.slider("Enter Petal Length (cm)", 1.0, 7.0, step=0.1)
        petal_width = st.slider("Enter Petal Width (cm)", 0.1, 3.0, step=0.1)

    prediction = get_prediction(sepal_length, sepal_width, petal_length, petal_width)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Prediction", prediction)
    with col2:
        with st.spinner("Loading image..."):
            show_image(prediction)
