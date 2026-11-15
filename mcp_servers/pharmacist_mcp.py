from fastmcp import FastMCP

mcp = FastMCP("Pharmacist")

# Simple in-memory drug database for demo purposes
DRUG_INFO = {
    "ibuprofen": "Pain reliever and fever reducer (NSAID). Usual adult dose: 200-400 mg every 4-6 hours.",
    "paracetamol": "Pain reliever and fever reducer. Usual adult dose: 500-1000 mg every 4-6 hours.",
    "amoxicillin": "Antibiotic used for bacterial infections. Usual adult dose: 250-500 mg every 8 hours.",
}

DRUG_INTERACTIONS = {
    ("ibuprofen", "aspirin"): "Increased risk of stomach bleeding.",
    ("amoxicillin", "warfarin"): "May increase the effect of warfarin, raising bleeding risk.",
}


@mcp.tool()
def get_drug_info(drug_name: str) -> str:
    """Get basic information about a medication."""
    drug_name = drug_name.lower()
    if drug_name in DRUG_INFO:
        return DRUG_INFO[drug_name]
    return f"No information found for '{drug_name}'."


@mcp.tool()
def check_drug_interaction(drug_a: str, drug_b: str) -> str:
    """Check if two medications have a known interaction."""
    pair = tuple(sorted([drug_a.lower(), drug_b.lower()]))
    if pair in DRUG_INTERACTIONS:
        return DRUG_INTERACTIONS[pair]
    return f"No known interaction found between '{drug_a}' and '{drug_b}'."


@mcp.tool()
def calculate_dose(weight_kg: float, dose_mg_per_kg: float) -> float:
    """Calculate a weight-based drug dose in mg."""
    return weight_kg * dose_mg_per_kg


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8001)
