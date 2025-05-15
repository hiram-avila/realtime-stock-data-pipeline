# Real-Time ML Streaming Demo

**Demo project** showcasing:

- ✅ Real-time stream processing with Kafka, Faust & Spark
- ✅ Machine Learning model training & inference (TensorFlow)
- ✅ Cloud-ready, scalable architecture patterns
- ✅ Interactive data visualization with Streamlit & Plotly

## Estructura
- **producer/**: Genera datos de ejemplo desde yfinance a Kafka
- **consumer/**: Procesa streams con Spark Streaming y Faust
- **ml/**: Código de entrenamiento y serialización de modelos
- **streamlit_app/**: Dashboard en Streamlit para visualización en tiempo real
- **infra/terraform**: Infraestructura como código para desplegar en AWS

## Requisitos
```bash
pip install -r requirements.txt
