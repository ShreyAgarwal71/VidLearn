import csv

# Input data as a string
input_data = """FILE 1
Emily: 75| Likes: Clean design, clear call to action| Dislikes: Generic imagery, lacks specific value propositions.
Michael: 70| Likes: Clear options for business users| Dislikes: Not enough technical details, too focused on broad appeal.
Sarah: 65| Likes: Simple and direct messaging| Dislikes: Not visually engaging enough for social media generation, not enough detail.
David: 50| Likes: Large, clear text| Dislikes: Too much text, confusing navigation for a retiree.
Alex: 60| Likes: Clean layout, minimal design | Dislikes: Generic imagery, lacks creativity and distinctive design elements.
Carlos: 80| Likes: Business-focused option| Dislikes: Lacks data/case studies, not enough information on ROI.
Lisa: 65| Likes: Easy to understand messaging | Dislikes: Not family-oriented, too corporate for her needs.
Brandon: 55| Likes: Straightforward language| Dislikes: Too generic, not relevant to his work, doesn't mention hardware.
Katie: 70| Likes: Simple design, business option link| Dislikes: Lacks details about remote work benefits, not personalized enough.
Sean: 50| Likes: Clear navigation to "About Windows"| Dislikes: Too promotional, lacks academic/technical documentation links.

FILE 2
Emily: 75| Likes: Fast shipping offer, familiar layout| Dislikes: Could feel generic, overwhelming product selection

Michael: 65| Likes: Established brand, wide product range| Dislikes: Information overload, potentially unsecured browsing

Sarah: 80| Likes: Affordable options, student discounts| Dislikes: Can get lost in the variety, potential for impulse buys

David: 50| Likes: Recognizable name, familiar categories| Dislikes: Too cluttered, overwhelming navigation

Alex: 70| Likes: Vast selection, design-related product access| Dislikes: Not visually curated, product quality concerns

Carlos: 70| Likes: Data-driven reviews, quick procurement| Dislikes: Scalability concerns, lack of customization options

Lisa: 85| Likes: Wide selection of family products, easy purchasing| Dislikes: Time sink, potential for overspending

Brandon: 60| Likes: Practical product selection, competitive pricing| Dislikes: Overwhelming interface, deceptive product quality

Katie: 75| Likes: Convenient for remote shopping, wide product selection| Dislikes: Time-consuming browsing, reliability concerns

Sean: 55| Likes: Access to diverse products, academic resources| Dislikes: Information overload, unreliable information sources

FILE 3
Emily: 75| Likes: Modern design, futuristic feel| Dislikes: Not immediately clear on career page access.

Michael: 60| Likes: Clean layout, focus on tunnels| Dislikes: Needs more technical specs.

Sarah: 85| Likes: Eye-catching visuals, "Burnt Hair" section| Dislikes: Might seem a little corporate.

David: 40| Likes: Simple design, easy to read text| Dislikes: Confusing navigation, too futuristic.

Alex: 90| Likes: Strong aesthetic, cool visuals| Dislikes: Needs more design-focused content.

Carlos: 70| Likes: Ambitious projects, clear statement about Dubai deal| Dislikes: Needs more data on cost-effectiveness.

Lisa: 55| Likes: Practical solutions messaging| Dislikes: Not family-oriented, flamethrower link.

Brandon: 65| Likes: Tunnels and Projects| Dislikes: Not enough practical use cases.

Katie: 70| Likes: Simple, uncluttered| Dislikes: Not enough to know about work opportunities.

Sean: 45| Likes: Clear titles| Dislikes: Superficial, not research focused.

FILE 4
Emily: 75| Likes: Clean design, product focus| Dislikes: Cookie notification, limited information on benefits.
Michael: 60| Likes: Simple navigation| Dislikes: Lack of detailed product specs, prominent cookie notice.
Sarah: 80| Likes: Visually appealing, trendy vibe| Dislikes: Cookie pop-up, unclear call to action.
David: 40| Likes: Clear "Contact Us" link| Dislikes: Overwhelming visuals, cookie consent.
Alex: 85| Likes: Aesthetic, reflects lifestyle| Dislikes: Cookie notification, lack of creative portfolio link.
Carlos: 70| Likes: Clear product presentation| Dislikes: Limited data on ingredients, invasive cookie banner.
Lisa: 55| Likes: Simple layout, easy to navigate| Dislikes: intrusive pop-up cookie, lack of family-friendly appeal.
Brandon: 45| Likes: Basic product display| Dislikes: Too much emphasis on design, missing practical details, cookie stuff.
Katie: 65| Likes: Clean product image| Dislikes: Distracting cookie notice, lacks remote-work relevant info.
Sean: 30| Likes: Minimalist approach| Dislikes: Intrusive cookie policy, lack of scientific backing, no research references."""

input_data = input_data.replace("Name: ", "")
input_data = input_data.replace("Score: ", "")
input_data = input_data.replace("Likes: ", "")
input_data = input_data.replace("Dislikes: ", "")
input_data = input_data.replace(".", "")
input_data = input_data.replace(":", "|")
input_data = input_data.replace(",", "")

data = input_data


# Split data into rows
#rows = [row.split("|") for row in data.split("\n")]
rows = [row.split("|") for row in data.split("\n") if row.strip()]

# Define CSV file name
csv_filename = "reviews.csv"

# Write to CSV
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Score", "Like Description", "Dislike"])  # Column headers
    writer.writerows(rows)

print(f"CSV file '{csv_filename}' has been created successfully.")