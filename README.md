# Déploiement de modèle Deep Learning - CIFAR-10

Ce projet montre comment entraîner un modèle CNN simple sur CIFAR-10 avec TensorFlow/Keras et le déployer via Streamlit.

## Étapes
1. Entraînement d’un modèle CNN sur le dataset CIFAR-10.
2. Sauvegarde du modèle au format H5.
3. Déploiement via une application Streamlit interactive.

## Lancer le projet

```
pip install -r requirements.txt
streamlit run app.py
```

## Fichiers
- `model_deployment.ipynb` – Notebook d’entraînement.
- `app.py` – Application Streamlit.
- `model_cifar10.h5` – Modèle entraîné (à générer via le notebook).