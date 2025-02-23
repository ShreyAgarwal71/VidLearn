import csv
import re
import os 

# input as a string 
input_data = """
Emily: CurryShoes: 30|Price: 40|Design: 50|Reason: Not relevant to professional image or needs.
Emily: ChefT-Shirt: 10|Price: 30|Design: 20|Reason: Not relevant to professional image or needs.
Emily: TrendT-Shirt: 10|Price: 30|Design: 20|Reason: Not relevant to professional image or needs.
Emily: RockJacket: 70|Price: 60|Design: 70|Reason: If it was a more neutral color, she might buy it for gym trips.
Emily: RockBra: 60|Price: 60|Design: 60|Reason: If it was a more neutral color, she might buy it for gym trips.
Emily: RockLeggings: 70|Price: 60|Design: 70|Reason: If it was a more neutral color, she might buy it for gym trips.
Michael: CurryShoes: 20|Price: 30|Design: 30|Reason: Not related to his needs or interests.
Michael: ChefT-Shirt: 10|Price: 40|Design: 20|Reason: Doesn't align with his style or needs.
Michael: TrendT-Shirt: 10|Price: 40|Design: 20|Reason: Doesn't align with his style or needs.
Michael: RockJacket: 30|Price: 40|Design: 30|Reason: Doesn't suit his style or IT work needs.
Michael: RockBra: 10|Price: 20|Design: 10|Reason: Not applicable.
Michael: RockLeggings: 10|Price: 20|Design: 10|Reason: Not applicable.
Sarah: CurryShoes: 85|Price: 70|Design: 90|Reason: 
Sarah: ChefT-Shirt: 75|Price: 80|Design: 75|Reason: If it was a bit more trendy.
Sarah: TrendT-Shirt: 75|Price: 80|Design: 75|Reason: If it had a more unique design.
Sarah: RockJacket: 70|Price: 50|Design: 65|Reason: If it was more affordable, and in a trendier color.
Sarah: RockBra: 65|Price: 60|Design: 60|Reason: If it was cheaper and came in a trendy color.
Sarah: RockLeggings: 70|Price: 60|Design: 65|Reason: If they were a bit cheaper and in a more appealing color.
David: CurryShoes: 10|Price: 20|Design: 10|Reason: Unlikely to purchase athletic shoes.
David: ChefT-Shirt: 5|Price: 10|Design: 5|Reason: No interest in sports-themed apparel.
David: TrendT-Shirt: 5|Price: 10|Design: 5|Reason: No interest in sports-themed apparel.
David: RockJacket: 10|Price: 20|Design: 10|Reason: No need for athletic wear.
David: RockBra: 1|Price: 1|Design: 1|Reason: Not applicable.
David: RockLeggings: 1|Price: 1|Design: 1|Reason: Not applicable.
Alex: CurryShoes: 40|Price: 50|Design: 50|Reason: Not their typical style.
Alex: ChefT-Shirt: 60|Price: 70|Design: 60|Reason: If the design were more artistic.
Alex: TrendT-Shirt: 65|Price: 70|Design: 70|Reason: If it had a more unique or artistic design.
Alex: RockJacket: 80|Price: 65|Design: 85|Reason: If it came in unique color combinations.
Alex: RockBra: 75|Price: 70|Design: 80|Reason: If it were available in more unique patterns or colors.
Alex: RockLeggings: 80|Price: 70|Design: 85|Reason: If they came in interesting patterns.
Carlos: CurryShoes: 30|Price: 40|Design: 30|Reason: Doesn't align with his needs.
Carlos: ChefT-Shirt: 10|Price: 20|Design: 10|Reason: Not relevant to professional or personal needs.
Carlos: TrendT-Shirt: 10|Price: 20|Design: 10|Reason: Not relevant to professional or personal needs.
Carlos: RockJacket: 40|Price: 50|Design: 40|Reason: Not aligned with his lifestyle or professional image.
Carlos: RockBra: 1|Price: 1|Design: 1|Reason: Not applicable.
Carlos: RockLeggings: 1|Price: 1|Design: 1|Reason: Not applicable.
Lisa: CurryShoes: 30|Price: 40|Design: 30|Reason: Not a priority for her current needs.
Lisa: ChefT-Shirt: 70|Price: 75|Design: 70|Reason: If it were on sale, she might buy it for her child.
Lisa: TrendT-Shirt: 70|Price: 75|Design: 70|Reason: If it were on sale, she might buy it for her child.
Lisa: RockJacket: 50|Price: 50|Design: 40|Reason: Doesn't fit her practical, family-focused lifestyle.
Lisa: RockBra: 40|Price: 40|Design: 40|Reason: Doesn't fit her lifestyle.
Lisa: RockLeggings: 50|Price: 50|Design: 40|Reason: Doesn't fit her lifestyle.
Brandon: CurryShoes: 50|Price: 50|Design: 50|Reason: Not a priority purchase.
Brandon: ChefT-Shirt: 65|Price: 70|Design: 60|Reason: If it was on clearance.
Brandon: TrendT-Shirt: 65|Price: 70|Design: 60|Reason: If it was on clearance.
Brandon: RockJacket: 40|Price: 30|Design: 30|Reason: Doesn't align with his practical work needs.
Brandon: RockBra: 1|Price: 1|Design: 1|Reason: Not applicable.
Brandon: RockLeggings: 1|Price: 1|Design: 1|Reason: Not applicable.
Katie: CurryShoes: 50|Price: 60|Design: 50|Reason: Not really something she would need.
Katie: ChefT-Shirt: 30|Price: 50|Design: 30|Reason: Not her style.
Katie: TrendT-Shirt: 30|Price: 50|Design: 30|Reason: Not her style.
Katie: RockJacket: 85|Price: 75|Design: 90|Reason: 
Katie: RockBra: 80|Price: 75|Design: 85|Reason: 
Katie: RockLeggings: 85|Price: 80|Design: 90|Reason: 
Sean: CurryShoes: 10|Price: 20|Design: 10|Reason: Not relevant to his needs.
Sean: ChefT-Shirt: 5|Price: 10|Design: 5|Reason: Not relevant to his needs.
Sean: TrendT-Shirt: 5|Price: 10|Design: 5|Reason: Not relevant to his needs.
Sean: RockJacket: 10|Price: 20|Design: 10|Reason: Not aligned with his priorities.
Sean: RockBra: 1|Price: 1|Design: 1|Reason: Not applicable.
Sean: RockLeggings: 1|Price: 1|Design: 1|Reason: Not applicable.

Emily: Project Rock 7: 70|100|75| If it was marketed as boosting performance and productivity, she'd buy it.
Emily: Unstoppable Fleece: 85|90|80|
Emily: Meridian Mesh: 90|95|85|
Emily: Apparition Shoes: 65|80|60| If they highlighted its versatility for both work and casual wear, she'd buy it.
Emily: Unstoppable Fleece Grid: 40|50|40|
Emily: Heavyweight Tonal: 30|40|30|
Michael: Project Rock 7: 30|50|30|
Michael: Unstoppable Fleece: 40|60|40|
Michael: Meridian Mesh: 20|30|20|
Michael: Apparition Shoes: 70|80|70| If it was marketed as durable and long-lasting, he'd buy it.
Michael: Unstoppable Fleece Grid: 85|90|80|
Michael: Heavyweight Tonal: 80|90|90| If the product was advertised as a comfortable layer for work and home he would buy it.
Sarah: Project Rock 7: 80|80|60| If the product was more trendy it would appeal to her.
Sarah: Unstoppable Fleece: 90|90|90|
Sarah: Meridian Mesh: 95|100|95|
Sarah: Apparition Shoes: 85|90|75|
Sarah: Unstoppable Fleece Grid: 60|70|60| If it came in brighter, more vibrant colors, she'd buy it.
Sarah: Heavyweight Tonal: 40|50|40|
David: Project Rock 7: 10|20|10|
David: Unstoppable Fleece: 70|80|80| If it was known for being comfortable for everyday wear, he'd buy it.
David: Meridian Mesh: 5|10|5|
David: Apparition Shoes: 30|40|30|
David: Unstoppable Fleece Grid: 40|50|40|
David: Heavyweight Tonal: 60|70|70| If it was endorsed by someone he trusted, he'd buy it.
Alex: Project Rock 7: 70|80|75| If it was marketed as edgy and unique, they'd buy it.
Alex: Unstoppable Fleece: 80|80|80| If the fleece was highlighted as being for layering and creating a unique design it would appeal.
Alex: Meridian Mesh: 95|90|100|
Alex: Apparition Shoes: 90|90|90|
Alex: Unstoppable Fleece Grid: 95|90|95|
Alex: Heavyweight Tonal: 85|90|85|
Carlos: Project Rock 7: 60|70|60| If it was highlighted as the leading gear and brand on the market, he'd buy it.
Carlos: Unstoppable Fleece: 30|40|30|
Carlos: Meridian Mesh: 20|30|20|
Carlos: Apparition Shoes: 50|60|50|
Carlos: Unstoppable Fleece Grid: 40|50|40|
Carlos: Heavyweight Tonal: 80|90|85| If the product was a symbol of leading a team and representing his ideals he would buy it.
Lisa: Project Rock 7: 20|30|20|
Lisa: Unstoppable Fleece: 90|95|90|
Lisa: Meridian Mesh: 40|50|40|
Lisa: Apparition Shoes: 75|80|80| If it was marketed as easy to clean and durable, she'd buy it.
Lisa: Unstoppable Fleece Grid: 60|70|70| If it was marketed for versatility, she'd buy it.
Lisa: Heavyweight Tonal: 70|80|75| If the product was comfortable for both indoors and outdoors she would buy it.
Brandon: Project Rock 7: 80|80|80|If it was known for being the premier training shoe for working men he would buy it.
Brandon: Unstoppable Fleece: 70|80|80| If the fleece was known for warmth and durability, he'd buy it.
Brandon: Meridian Mesh: 10|20|10|
Brandon: Apparition Shoes: 90|90|90|
Brandon: Unstoppable Fleece Grid: 80|80|80| If the product was advertised as protecting against the elements and durable he would buy it.
Brandon: Heavyweight Tonal: 90|90|90|
Katie: Project Rock 7: 50|60|50|
Katie: Unstoppable Fleece: 95|100|95|
Katie: Meridian Mesh: 80|80|80| If it was marketed as comfortable for working from home, she'd buy it.
Katie: Apparition Shoes: 80|80|80| If they had great arch support, she'd buy it.
Katie: Unstoppable Fleece Grid: 85|90|85|
Katie: Heavyweight Tonal: 90|90|90|
Sean: Project Rock 7: 20|30|20|
Sean: Unstoppable Fleece: 80|90|90| If it was known for warmth, he'd buy it.
Sean: Meridian Mesh: 5|10|5|
Sean: Apparition Shoes: 40|50|40|
Sean: Unstoppable Fleece Grid: 60|70|70| If it was known to protect against the elements, he'd buy it.
Sean: Heavyweight Tonal: 70|80|80| If the product was warm and comfortable he would buy it.

Emily: Curry Fox 1: 65| 70| 80| If they came in a color more suitable for business casual, she would buy them.
Emily: UA Icon Hoodie: 75| 70| 80| A more muted, professional color would make her buy it.
Emily: HeatGear Long Sleeve: 55| 80| 80|
Emily: UA Performance Boxerjock: 20| 90| 20|
Emily: UA Icon Fleece Shorts: 30| 80| 60|
Emily: Project Rock Shoes: 85| 70| 80|
Michael: Curry Fox 1: 20| 50| 50|
Michael: UA Icon Hoodie: 80| 70| 70| He would buy it if it had better weather protection.
Michael: HeatGear Long Sleeve: 90| 80| 85|
Michael: UA Performance Boxerjock: 10| 80| 20|
Michael: UA Icon Fleece Shorts: 40| 70| 70|
Michael: Project Rock Shoes: 90| 75| 80|
Sarah: Curry Fox 1: 90| 60| 85|
Sarah: UA Icon Hoodie: 95| 80| 90|
Sarah: HeatGear Long Sleeve: 60| 80| 70| A trendier design would entice her to buy it.
Sarah: UA Performance Boxerjock: 90| 90| 95|
Sarah: UA Icon Fleece Shorts: 95| 70| 90|
Sarah: Project Rock Shoes: 90| 70| 85|
David: Curry Fox 1: 10| 50| 20|
David: UA Icon Hoodie: 50| 70| 60|
David: HeatGear Long Sleeve: 30| 70| 40|
David: UA Performance Boxerjock: 5| 90| 10|
David: UA Icon Fleece Shorts: 20| 70| 30|
David: Project Rock Shoes: 30| 70| 40|
Alex: Curry Fox 1: 80| 60| 80| A bolder, more unique colorway would persuade them.
Alex: UA Icon Hoodie: 90| 80| 90|
Alex: HeatGear Long Sleeve: 60| 80| 70| A more artistic or edgy design would make them buy it.
Alex: UA Performance Boxerjock: 95| 90| 95|
Alex: UA Icon Fleece Shorts: 90| 70| 90|
Alex: Project Rock Shoes: 90| 70| 85|
Carlos: Curry Fox 1: 30| 60| 50|
Carlos: UA Icon Hoodie: 60| 70| 70| A more professional cut and style would get him to buy it.
Carlos: HeatGear Long Sleeve: 70| 80| 70| Higher performance metrics would make him buy it.
Carlos: UA Performance Boxerjock: 30| 90| 20|
Carlos: UA Icon Fleece Shorts: 40| 70| 60|
Carlos: Project Rock Shoes: 95| 70| 80|
Lisa: Curry Fox 1: 30| 60| 40|
Lisa: UA Icon Hoodie: 80| 70| 70| If it were easier to clean, she would buy it.
Lisa: HeatGear Long Sleeve: 60| 80| 70| If it had additional practical features for moms, she'd consider buying it.
Lisa: UA Performance Boxerjock: 5| 90| 10|
Lisa: UA Icon Fleece Shorts: 60| 70| 70| More modest coverage would make her buy it.
Lisa: Project Rock Shoes: 70| 70| 80| More stain resistant material would entice her.
Brandon: Curry Fox 1: 20| 50| 40|
Brandon: UA Icon Hoodie: 80| 70| 70| More durability would convince him.
Brandon: HeatGear Long Sleeve: 85| 80| 85|
Brandon: UA Performance Boxerjock: 80| 90| 70| Additional durability would make him buy them.
Brandon: UA Icon Fleece Shorts: 70| 70| 70| Higher durability would make him buy it.
Brandon: Project Rock Shoes: 90| 70| 80|
Katie: Curry Fox 1: 50| 60| 60|
Katie: UA Icon Hoodie: 90| 80| 90|
Katie: HeatGear Long Sleeve: 70| 80| 70| Extra features for outdoor activity would make her buy it.
Katie: UA Performance Boxerjock: 5| 90| 10|
Katie: UA Icon Fleece Shorts: 85| 70| 80|
Katie: Project Rock Shoes: 95| 70| 90|
Sean: Curry Fox 1: 10| 50| 20|
Sean: UA Icon Hoodie: 20| 70| 30|
Sean: HeatGear Long Sleeve: 20| 70| 30|
Sean: UA Performance Boxerjock: 5| 90| 10|
Sean: UA Icon Fleece Shorts: 10| 70| 20|
Sean: Project Rock Shoes: 10| 70| 20|

Emily: Unisex UA SlipSpeed Mega Fade Shoes| Score: 70| Price: 60| Design: 80| If they came in more colors, I would consider buying them.
Emily: Men's UA Icon Charged Cotton Short Sleeve| Score: 70| Price: 90| Design: 65| I would consider buying them if there were more stylish colors available.
Emily: Men's UA Unstoppable Tapered Pants| Score: 85| Price: 70| Design: 80|
Emily: Men's UA Phantom 1 Shoes| Score: 65| Price: 60| Design: 70| If these came in a different style, I would buy them.
Emily: Men's UA Left Chest Logo Short Sleeve| Score: 50| Price: 90| Design: 40| Reason:
Emily: Unisex UA SpeedForm Gemini Running Shoes| Score: 80| Price: 70| Design: 80| If they came in a color that I liked, I would consider buying them.
Michael: Unisex UA SlipSpeed Mega Fade Shoes| Score: 30| Price: 40| Design: 30| Reason:
Michael: Men's UA Icon Charged Cotton Short Sleeve| Score: 70| Price: 90| Design: 70| I would consider buying them if the material were moisture-wicking.
Michael: Men's UA Unstoppable Tapered Pants| Score: 80| Price: 80| Design: 70| If the material was more durable, I would buy them.
Michael: Men's UA Phantom 1 Shoes| Score: 40| Price: 50| Design: 40| Reason:
Michael: Men's UA Left Chest Logo Short Sleeve| Score: 70| Price: 95| Design: 70| If the fabric were more durable, I would buy them.
Michael: Unisex UA SpeedForm Gemini Running Shoes| Score: 50| Price: 50| Design: 50| Reason:
Sarah: Unisex UA SlipSpeed Mega Fade Shoes| Score: 75| Price: 80| Design: 80| I would buy these if they were more trendy.
Sarah: Men's UA Icon Charged Cotton Short Sleeve| Score: 80| Price: 95| Design: 80| If there were more colors, I would consider buying them.
Sarah: Men's UA Unstoppable Tapered Pants| Score: 90| Price: 70| Design: 80|
Sarah: Men's UA Phantom 1 Shoes| Score: 85| Price: 80| Design: 80|
Sarah: Men's UA Left Chest Logo Short Sleeve| Score: 95| Price: 100| Design: 90|
Sarah: Unisex UA SpeedForm Gemini Running Shoes| Score: 75| Price: 70| Design: 70| I would buy these if they were more colorful.
David: Unisex UA SlipSpeed Mega Fade Shoes| Score: 20| Price: 30| Design: 20| Reason:
David: Men's UA Icon Charged Cotton Short Sleeve| Score: 90| Price: 100| Design: 100|
David: Men's UA Unstoppable Tapered Pants| Score: 40| Price: 50| Design: 40| Reason:
David: Men's UA Phantom 1 Shoes| Score: 10| Price: 10| Design: 10| Reason:
David: Men's UA Left Chest Logo Short Sleeve| Score: 90| Price: 100| Design: 100|
David: Unisex UA SpeedForm Gemini Running Shoes| Score: 30| Price: 40| Design: 30| Reason:
Alex: Unisex UA SlipSpeed Mega Fade Shoes| Score: 80| Price: 70| Design: 80| If there were more unique designs, I would buy them.
Alex: Men's UA Icon Charged Cotton Short Sleeve| Score: 80| Price: 90| Design: 80| If there were more artistic designs, I would buy them.
Alex: Men's UA Unstoppable Tapered Pants| Score: 80| Price: 70| Design: 80| If these were more unique, I would consider buying them.
Alex: Men's UA Phantom 1 Shoes| Score: 80| Price: 70| Design: 80| If these came in a brighter color I would be more inclined to purchase.
Alex: Men's UA Left Chest Logo Short Sleeve| Score: 80| Price: 95| Design: 80| If there were more colors I would consider buying.
Alex: Unisex UA SpeedForm Gemini Running Shoes| Score: 80| Price: 70| Design: 80| If they were more trendy, I would buy them.
Carlos: Unisex UA SlipSpeed Mega Fade Shoes| Score: 60| Price: 50| Design: 50| If there were more data on performance, I would consider buying these.
Carlos: Men's UA Icon Charged Cotton Short Sleeve| Score: 80| Price: 90| Design: 70| If I knew the material breathability, I would buy this shirt.
Carlos: Men's UA Unstoppable Tapered Pants| Score: 70| Price: 70| Design: 60| If these pants were tested for athletic activity I would buy these.
Carlos: Men's UA Phantom 1 Shoes| Score: 60| Price: 60| Design: 60| If I knew how well it would perform, I would buy it.
Carlos: Men's UA Left Chest Logo Short Sleeve| Score: 80| Price: 95| Design: 70| If this shirt had data on performance I would buy.
Carlos: Unisex UA SpeedForm Gemini Running Shoes| Score: 60| Price: 50| Design: 50| If there were more reviews, I would be more inclined to buy.
Lisa: Unisex UA SlipSpeed Mega Fade Shoes| Score: 40| Price: 50| Design: 40| Reason:
Lisa: Men's UA Icon Charged Cotton Short Sleeve| Score: 70| Price: 95| Design: 80| If this shirt had stain-resistant material, I would buy it.
Lisa: Men's UA Unstoppable Tapered Pants| Score: 60| Price: 60| Design: 70| If these pants were stain-resistant, I would buy them.
Lisa: Men's UA Phantom 1 Shoes| Score: 30| Price: 40| Design: 30| Reason:
Lisa: Men's UA Left Chest Logo Short Sleeve| Score: 85| Price: 95| Design: 90|
Lisa: Unisex UA SpeedForm Gemini Running Shoes| Score: 50| Price: 60| Design: 50| Reason:
Brandon: Unisex UA SlipSpeed Mega Fade Shoes| Score: 20| Price: 30| Design: 20| Reason:
Brandon: Men's UA Icon Charged Cotton Short Sleeve| Score: 85| Price: 95| Design: 90|
Brandon: Men's UA Unstoppable Tapered Pants| Score: 90| Price: 70| Design: 80|
Brandon: Men's UA Phantom 1 Shoes| Score: 10| Price: 20| Design: 10| Reason:
Brandon: Men's UA Left Chest Logo Short Sleeve| Score: 90| Price: 100| Design: 100|
Brandon: Unisex UA SpeedForm Gemini Running Shoes| Score: 30| Price: 40| Design: 30| Reason:
Katie: Unisex UA SlipSpeed Mega Fade Shoes| Score: 80| Price: 70| Design: 80| If there were more reviews, I would buy these.
Katie: Men's UA Icon Charged Cotton Short Sleeve| Score: 70| Price: 90| Design: 70| If this shirt had better moisture-wicking, I would buy it.
Katie: Men's UA Unstoppable Tapered Pants| Score: 95| Price: 80| Design: 90|
Katie: Men's UA Phantom 1 Shoes| Score: 70| Price: 60| Design: 60| If these shoes were tested for long distances I would buy these.
Katie: Men's UA Left Chest Logo Short Sleeve| Score: 85| Price: 95| Design: 90|
Katie: Unisex UA SpeedForm Gemini Running Shoes| Score: 80| Price: 70| Design: 80| If these shoes were more comfortable I would buy these.
Sean: Unisex UA SlipSpeed Mega Fade Shoes| Score: 40| Price: 50| Design: 40| Reason:
Sean: Men's UA Icon Charged Cotton Short Sleeve| Score: 90| Price: 100| Design: 100|
Sean: Men's UA Unstoppable Tapered Pants| Score: 50| Price: 60| Design: 50| Reason:
Sean: Men's UA Phantom 1 Shoes| Score: 20| Price: 30| Design: 20| Reason:
Sean: Men's UA Left Chest Logo Short Sleeve| Score: 90| Price: 100| Design: 100|
Sean: Unisex UA SpeedForm Gemini Running Shoes| Score: 30| Price: 40| Design: 30| Reason:

"""

def remove_lines_with_pattern(text, pattern=r"\*\*.*?\*\*"):
    lines = text.split("\n")
    filtered_lines = [line for line in lines if not re.search(pattern, line)]
    return "\n".join(filtered_lines)

def remove_empty_lines(text):
    lines = text.split("\n")
    non_empty_lines = [line for line in lines if line.strip()] 
    return "\n".join(non_empty_lines)

input_data = remove_lines_with_pattern(input_data)
input_data = remove_empty_lines(input_data)

os.makedirs("csvFolderUpdated", exist_ok=True)

input_data = input_data.replace("Name: ", "")
input_data = input_data.replace("Product: ", "")
input_data = input_data.replace("Score: ", "")
input_data = input_data.replace("Price: ", "")
input_data = input_data.replace("Design: ", "")
input_data = input_data.replace("Dislikes: ", "")
input_data = input_data.replace("Reason:", "")
input_data = input_data.replace("N/A", "")
input_data = input_data.replace("Not applicable.", "")
input_data = input_data.replace(".", "")
input_data = input_data.replace(":", "|")
input_data = input_data.replace(",", "")

data = input_data

#print (data)

lines = data.split('\n')

allProducts = []
temp = []
for x in lines:
    temp = x.split('|')
    if temp[1] not in allProducts:
        allProducts.append(temp[1])

print(allProducts)
print(len(allProducts))

#rows = [row.split("|") for row in data.split("\n")]
rows = [row.split("|") for row in data.split("\n") if row.strip()]


for product_index, product in enumerate(allProducts):
    product_rows = []
    
    for line in rows:
        if product in line[1]:

            name = line[0].strip()
            score = line[2].strip() if len(line) > 2 else ""
            price = line[3].strip() if len(line) > 3 else ""
            design = line[4].strip() if len(line) > 4 else ""
            reason = line[5].strip() if len(line) > 5 else ""
            
            product_rows.append([name, score, price, design, reason])

    csv_filename = "csvFolder/" + product + f"{product_index + 1:02d}.csv"


    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score", "Price", "Design", "Reason"])  # Column headers
        writer.writerows(product_rows)

    print(f"CSV file '{csv_filename}' has been created successfully.")



folder_path = 'csvFolder'
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if filename.endswith('.csv'):
        try:
            with open(file_path, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                lines = list(reader)
                
                # only keep if 11 or 12
                if len(lines) not in [11, 12]:
                    os.remove(file_path)

        except Exception as e:
            print(f"Error processing {filename}: {e}")



