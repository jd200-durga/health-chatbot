import json

# Load dataset
with open("data/health_data.json") as f:
    data = json.load(f)

diseases = data["diseases"]
first_aid = data["first_aid"]
nutrition = data["nutrition_tips"]
emergency = data["emergency_numbers"]


def get_response(message):

    msg = message.lower()

    # ---------------- DISEASE RESPONSE ----------------
    for disease in diseases:
        if disease in msg:

            info = diseases[disease]

            symptoms = ", ".join(info["symptoms"])
            prevention = ", ".join(info["prevention"])
            treatment = info["treatment"]

            return f"""
Disease: {disease.upper()}

Symptoms:
{symptoms}

Prevention:
{prevention}

Treatment:
{treatment}
"""

    # ---------------- EMERGENCY NUMBERS ----------------
    if "emergency" in msg or "helpline" in msg or "help number" in msg:

        return f"""
Emergency Numbers:

National Health Helpline: {emergency['national_health_helpline']}
Ambulance: {emergency['ambulance']}
Women's Helpline: {emergency['womens_helpline']}
Child Helpline: {emergency['child_helpline']}
COVID Helpline: {emergency['covid_helpline']}
Disaster Management: {emergency['disaster_management']}
"""

    # ---------------- FIRST AID ----------------
    for aid in first_aid:
        if aid in msg:

            return f"""
First Aid for {aid.upper()}:

{first_aid[aid]}
"""

    # ---------------- NUTRITION TIPS ----------------

    if "nutrition" in msg or "diet" in msg or "food tips" in msg:

        if "children" in msg or "kids" in msg:

            children = "\n".join(nutrition["children"])

            return f"""
Nutrition Tips for Children:

{children}
"""

    elif "pregnant" in msg or "pregnancy" in msg:

        pregnant = "\n".join(nutrition["pregnant"])

        return f"""
Nutrition Tips for Pregnant Women:

{pregnant}
"""

    elif "general" in msg or "adult" in msg:

        general = "\n".join(nutrition["general"])

        return f"""
General Nutrition Tips:

{general}
"""

    else:

        return """
Please specify the category:

• nutrition tips for children  
• nutrition tips for pregnant women  
• general nutrition tips
"""

    return "Ask about diseases (dengue, malaria), first aid (burns, fever), nutrition tips, or emergency numbers."
