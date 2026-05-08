class HospitalExpertSystem:

    def __init__(self):

        # Knowledge Base (Rules)
        self.rules = [

            {
                "condition": lambda s, sev: s == "chest pain" and sev == "high",

                "action": "Emergency Cardiology Unit required immediately."
            },

            {
                "condition": lambda s, sev: s == "breathing problem" and sev == "high",

                "action": "Shift patient to ICU and provide oxygen support."
            },

            {
                "condition": lambda s, sev: s == "fever" and sev == "low",

                "action": "Consult General Physician and prescribe basic medication."
            },

            {
                "condition": lambda s, sev: s == "fracture",

                "action": "Refer patient to Orthopedic Department for X-Ray."
            },

            {
                "condition": lambda s, sev: s == "skin allergy",

                "action": "Refer patient to Dermatology Department."
            },

            {
                "condition": lambda s, sev: sev == "critical",

                "action": "Immediate emergency admission and senior doctor consultation."
            }

        ]


    # Inference Engine
    def inference_engine(self, symptom, severity):

        for rule in self.rules:

            if rule["condition"](symptom, severity):

                return rule["action"]

        return "No exact match found. Refer to General OPD."


# ---------------- MAIN PROGRAM ----------------

system = HospitalExpertSystem()

patients = [

    {
        "name": "Rahul",
        "symptom": "chest pain",
        "severity": "high"
    },

    {
        "name": "Sneha",
        "symptom": "fever",
        "severity": "low"
    },

    {
        "name": "Amit",
        "symptom": "fracture",
        "severity": "medium"
    },

    {
        "name": "Priya",
        "symptom": "breathing problem",
        "severity": "high"
    }

]

print("------ Hospital Expert System ------\n")

for patient in patients:

    recommendation = system.inference_engine(
        patient["symptom"],
        patient["severity"]
    )

    print(f"Patient Name : {patient['name']}")
    print(f"Symptom      : {patient['symptom']}")
    print(f"Severity     : {patient['severity']}")
    print(f"Recommendation: {recommendation}")

    print("-" * 50)
