# Bayan: AI Platform for Learning Saudi Sign Language

## Overview 
Bayan is an AI-powered web platform designed to make learning Saudi Sign Language (SSL) accessible, interactive, and practical. With a real-time gesture recognition model and structured lessons, Bayan helps users of all backgrounds learn SSL — whether to communicate with loved ones, work as interpreters, or promote inclusivity.

## Features
1- Structured Lessons
Progressive chapters that teach you the Saudi alphabet and common words.
2- Real-Time AI Sign Practice
Use your webcam to practice gestures — get instant feedback powered by our CNN-based model.
3- Interactive Quizzes
Test your progress with quizzes that adapt to your lesson history.
4- Gesture Dictionary
A searchable sign language reference with video demonstrations.

## Problem We're Solving
Saudi Arabia has ~750,000 deaf/mute individuals… but only 103 official sign language translators. Most learning platforms are either static or tailored to American Sign Language (ASL). Bayan introduces an interactive, AI-assisted, and region-specific solution to address this gap.
Our mission is to normalize sign language learning, make it enjoyable, and increase societal inclusivity.

## AI Model Overview
1- Initial Model (VideoMAE)
We began with VideoMAE, a transformer-based model specialized in masked video autoencoding. It's built for understanding motion and temporal patterns in video data, making it a good theoretical match for gesture recognition.

2- Custom CNN-Based Classifier (CNN-based)
After dropping VideoMAE, we built a lightweight CNN model from scratch, optimized for classifying static hand gestures (one image per gesture). The shift in approach aligned better with our data and performance goals.

Final model shows strong gesture classification, but future improvements will include more gestures and better datasets.

## Dataset Summary
We used 5 major Arabic Sign Language datasets including:
- Arabic Sign Language Dataset 2022
- RGB Arabic Alphabets Dataset
- ARASL - Alphabet Sequences

## Future Enhancements
- Expand gesture support to full vocabulary
- Improve model with higher-quality, diverse data

## Team
- Nawaf Alhomaidhi
- Musaad Almansour
- Mohamad Alsharhan

## Conclusion 
Bayan is more than a graduation project — it’s a movement toward inclusivity. By integrating cutting-edge AI with a culturally specific need, we aim to empower both learners and the deaf/mute community in Saudi Arabia.
