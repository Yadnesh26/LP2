class InformationExpertSystem:
    def __init__(self):
        # Knowledge Base (Rules)
        self.rules = [
            {
                "condition": lambda s, v: s == "high" and v == "large",
                "action": "Store in Encrypted On-Premise Servers with strict access logs."
            },
            {
                "condition": lambda s, v: s == "high" and v == "small",
                "action": "Store in Hardware Security Module (HSM) or Offline Vault."
            },
            {
                "condition": lambda s, v: s == "low" and v == "large",
                "action": "Use Scalable Public Cloud Storage (e.g., AWS S3 / Google Cloud)."
            },
            {
                "condition": lambda s, v: s == "low" and v == "small",
                "action": "Standard Local Database or Spreadsheet is sufficient."
            },
            {
                # FIX: Proper condition (no exception hack)
                "condition": lambda s, v: s == "medium",
                "action": "Use Private Cloud with Multi-Factor Authentication (MFA)."
            }
        ]

    def inference_engine(self, sensitivity, volume):
        for rule in self.rules:
            if rule["condition"](sensitivity, volume):
                return rule["action"]

        return "No specific rule found. Consult a Data Architect."


# --- Test Data ---
system = InformationExpertSystem()

test_data = [
    {"type": "Financial Records", "sensitivity": "high", "volume": "large"},
    {"type": "Public Marketing Images", "sensitivity": "low", "volume": "large"},
    {"type": "Employee Passwords", "sensitivity": "high", "volume": "small"},
    {"type": "General Feedback", "sensitivity": "medium", "volume": "small"}
]

# --- Output ---
print("--- Information Management Expert System Output ---")
print(f"{'Data Type':<30} | {'Recommendation'}")
print("-" * 90)

for data in test_data:
    recommendation = system.inference_engine(data['sensitivity'], data['volume'])
    print(f"{data['type']:<30} | {recommendation}")