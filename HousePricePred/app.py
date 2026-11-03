
import streamlit as st

from src.predict import predict_house_price


st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered",
)


# The cities must match the synthetic training dataset.
LOCATIONS = [
    "Ahmedabad",
    "Bengaluru",
    "Bhubaneswar",
    "Chandigarh",
    "Chennai",
    "Delhi",
    "Hyderabad",
    "Indore",
    "Jaipur",
    "Kochi",
    "Kolkata",
    "Lucknow",
    "Mumbai",
    "Nagpur",
    "Pune",
]


st.title("🏠 House Price Prediction")
st.write(
    "Estimate a property's price using its location and "
    "basic characteristics."
)

st.info(
    "This application uses a synthetic dataset for educational "
    "purposes. Predictions are not verified market valuations."
)

st.divider()

st.subheader("Property Details")

with st.form("property_form"):
    location = st.selectbox(
        "Location",
        options=LOCATIONS,
        index=LOCATIONS.index("Bhubaneswar"),
    )

    area_sq_ft = st.number_input(
        "Area (square feet)",
        min_value=350,
        max_value=5500,
        value=1500,
        step=50,
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=6,
        value=3,
        step=1,
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=5,
        value=2,
        step=1,
    )

    property_age_years = st.number_input(
        "Property Age (years)",
        min_value=0,
        max_value=40,
        value=5,
        step=1,
    )

    submitted = st.form_submit_button(
        "Predict House Price",
        type="primary",
        use_container_width=True,
    )


if submitted:
    try:
        estimated_price = predict_house_price(
            location=location,
            area_sq_ft=area_sq_ft,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            property_age_years=property_age_years,
        )

        st.divider()
        st.subheader("Estimated Property Price")

        st.metric(
            label="Predicted Price",
            value=f"₹{estimated_price:,.0f}",
        )

        st.caption(
            f"Approximately ₹{estimated_price / 100000:.2f} lakh"
        )

        st.caption(
            "This is a model-generated estimate based on "
            "synthetic training data, not a real-market quote."
        )

    except (ValueError, FileNotFoundError) as exc:
        st.error(str(exc))

    except Exception:
        st.error(
            "Prediction failed. Check that the trained model "
            "exists and that the installed packages are correct."
        )


st.divider()
st.caption("House Price Prediction | Machine Learning Project")
