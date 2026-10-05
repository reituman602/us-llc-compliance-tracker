"""
US LLC Statutory Cost & Compliance Tracker for Non-Resident Founders
Maintained by KuajingBase (https://kuajingbase.com)
"""

STATE_DATA = {
    "michigan": {
        "name": "Michigan (LARA)",
        "initial_fee": 50,
        "annual_fee": 25,
        "due_date": "February 15",
        "privacy": "Moderate (Public Records)",
        "penalty": "$10/month late fee (dissolution risk after 2 years)",
    },
    "wyoming": {
        "name": "Wyoming (Secretary of State)",
        "initial_fee": 100,
        "annual_fee": 60,
        "due_date": "First day of anniversary month",
        "privacy": "Top Tier (Anonymous Members)",
        "penalty": "Administrative dissolution after 60 days",
    },
    "florida": {
        "name": "Florida (Sunbiz)",
        "initial_fee": 125,
        "annual_fee": 138.75,
        "due_date": "May 1 (Strict)",
        "privacy": "Moderate (Public Sunbiz Database)",
        "penalty": "$400 non-negotiable statutory late fee after May 1",
    },
    "delaware": {
        "name": "Delaware (Division of Corporations)",
        "initial_fee": 110,
        "annual_fee": 400,
        "due_date": "June 1 (Franchise Tax)",
        "privacy": "High (Members not publicly listed)",
        "penalty": "$200 late penalty + 1.5% monthly interest",
    },
    "illinois": {
        "name": "Illinois (CyberDriveIllinois)",
        "initial_fee": 150,
        "annual_fee": 75,
        "due_date": "First day of anniversary month",
        "privacy": "Moderate",
        "penalty": "1.5% PPRT tax risk for multi-member entities",
    }
}

def calculate_holding_cost(state_key, years=3):
    state = STATE_DATA.get(state_key.lower())
    if not state:
        print(f"State '{state_key}' not found in audit index.")
        return
    
    total = state["initial_fee"] + (state["annual_fee"] * years)
    print("\n" + "="*50)
    print(f"Jurisdiction: {state['name']}")
    print(f"Initial Formation Fee: ${state['initial_fee']}")
    print(f"Annual Filing Fee:     ${state['annual_fee']}/year (Due: {state['due_date']})")
    print(f"Total {years}-Year State Cost: ${total}")
    print(f"Privacy Rating:        {state['privacy']}")
    print(f"Statutory Penalty:     {state['penalty']}")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("--- US LLC Compliance & Statutory Holding Cost Calculator ---")
    print("Available states: Michigan, Wyoming, Florida, Delaware, Illinois\n")
    user_state = input("Enter state name: ").strip()
    calculate_holding_cost(user_state)
