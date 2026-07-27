CURRICULUM = [
    {
        "id": "python-basics",
        "title": "Python Basics",
        "level": "beginner",
        "topics": [
            "variables",
            "data types",
            "loops",
            "functions",
            "lists",
            "dictionaries"
        ]
    },
    {
        "id": "data-analysis",
        "title": "Data Analysis",
        "level": "beginner",
        "topics": [
            "NumPy",
            "Pandas",
            "data cleaning",
            "data visualization"
        ]
    },
    {
        "id": "math-for-ml",
        "title": "Math for Machine Learning",
        "level": "beginner",
        "topics": [
            "statistics",
            "probability",
            "linear algebra basics",
            "calculus basics"
        ]
    },
    {
        "id": "machine-learning",
        "title": "Machine Learning",
        "level": "intermediate",
        "topics": [
            "supervised learning",
            "unsupervised learning",
            "regression",
            "classification",
            "model evaluation"
        ]
    },
    {
        "id": "deep-learning",
        "title": "Deep Learning",
        "level": "advanced",
        "topics": [
            "neural networks",
            "CNN",
            "RNN",
            "transformers"
        ]
    },
    {
        "id": "mlops",
        "title": "MLOps",
        "level": "advanced",
        "topics": [
            "model deployment",
            "APIs",
            "Docker",
            "monitoring",
            "retraining"
        ]
    }
]


def get_curriculum_text():
    lines = []

    for module in CURRICULUM:
        lines.append(f"Module: {module['title']} ({module['level']})")
        lines.append("Topics: " + ", ".join(module["topics"]))
        lines.append("")

    return "\n".join(lines)
