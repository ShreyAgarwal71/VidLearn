from google import genai
from google.genai import types
import csv
import PIL.Image
import os
import re
import pandas as pd


def sanitize_filename(s):
    # Remove any characters that are not alphanumeric or underscores.
    return re.sub(r'\W+', '_', s)

def process_uploaded_files(file_paths, csv_folder):
    client = genai.Client(api_key="AIzaSyCZDI2WQbEAVhWH7AxasayTdkBK5yA5Uk8")
    
    text_example = '''
For each persona listed below, assume they are checking the catalog in the images. For each of the products in the catalogue image, think for and determine how likely each person would buy the product, as a number out of 100. Then have them give a number out of 100 rating the score, and a number out of 100 rating the price. If the number for the overall “score” is between 60 and 80, then give a sentence on what could change about the product that would then make the persona buy it. If the number is above 80, then leave the reason blank. Format the response according to the following:
remove any unnecessary text and spacing between, any additional text other than what i am going to give you should be removed. only give one line per persona and no other text. and here's exactly how your output should be generated:
Name: X| Product: X| Score: X| Price: X| Design: X| Reason: X

1. Emily – The Ambitious Millennial Professional
Age: 28
Gender: Female
Job: Digital Marketing Specialist at a mid-size agency
Education: Bachelor’s degree in Communications
Location: Urban center (e.g., Chicago)
Family Situation: Single but in a long-term relationship
Archetype: Ambitious Achiever
Goals: Rapid career progression, skill development, and expanding her professional network
Challenges: Balancing demanding work projects with personal life and managing work-related stress
Fears: Stagnating in her career or missing out on emerging opportunities
Problems: Overload from multiple projects and information overload from constant digital connectivity
Values: Innovation, continuous learning, and efficiency
Buying Decision Process: Conducts thorough online research, reads reviews, and is influenced by peer recommendations and brand reputation
Internet & Website Usage: Regularly uses LinkedIn for professional networking, visits industry blogs, and actively engages on platforms like Instagram and Twitter for both inspiration and networking

2. Michael – The Suburban IT Specialist
Age: 42
Gender: Male
Job: IT Manager at a mid-sized corporation
Education: Bachelor’s in Information Technology with multiple professional certifications
Location: Suburban area near a major city (e.g., Atlanta suburbs)
Family Situation: Married with two school-aged children
Archetype: Practical Problem-Solver
Goals: Secure his family’s future, streamline workplace technology, and maintain work-life balance
Challenges: Staying updated with rapidly evolving tech while juggling family responsibilities
Fears: Job obsolescence and cybersecurity threats affecting his company or family data
Problems: Struggling with time management and coping with overwhelming tech updates
Values: Reliability, security, and practical efficiency
Buying Decision Process: Reviews detailed product specifications, values expert opinions, and prefers brands with proven track records
Internet & Website Usage: Uses tech forums, professional development sites, and online retailers; frequently reads tech news and subscribes to industry newsletters

3. Sarah – The College Student Explorer
Age: 20
Gender: Female
Job: Part-time barista while pursuing higher education
Education: Currently studying for a Bachelor’s in Sociology
Location: University town (e.g., a lively college town in the Northeast)
Family Situation: Lives in shared housing with other students
Archetype: Trend Follower and Explorer
Goals: Excel academically, secure internships, and build a dynamic social network
Challenges: Balancing coursework, a part-time job, and active social life; managing tight finances
Fears: Falling behind in studies or missing key social and professional opportunities
Problems: Overcommitment and stress due to juggling multiple responsibilities
Values: Diversity, social responsibility, and community engagement
Buying Decision Process: Highly influenced by social media trends, peer reviews, and affordability; prioritizes budget-friendly choices
Internet & Website Usage: Heavy user of social platforms like Instagram and TikTok, utilizes online academic resources, and streams content for both education and entertainment

4. David – The Reflective Retiree
Age: 68
Gender: Male
Job: Retired engineer
Education: Bachelor’s degree in Engineering
Location: Small town (e.g., a quiet community in Maine)
Family Situation: Widowed; maintains close contact with adult children and grandchildren
Archetype: The Traditionalist and Reflective Thinker
Goals: Stay connected with loved ones, manage retirement finances wisely, and pursue hobbies
Challenges: Adapting to new digital tools and overcoming occasional technological frustrations
Fears: Social isolation and potential financial insecurity during retirement
Problems: Difficulty navigating modern website designs and digital platforms
Values: Family, stability, and trustworthiness
Buying Decision Process: Leans toward familiar brands, trusts recommendations from family and close friends, and prefers straightforward, reliable information
Internet & Website Usage: Uses websites for news, online banking, and social media (primarily Facebook) to keep in touch with family

5. Alex – The Creative Freelancer
Age: 34
Gender: Non-binary
Job: Freelance Graphic Designer
Education: Bachelor’s degree in Fine Arts
Location: Urban setting (e.g., Portland, Oregon)
Family Situation: Single; lives in a shared apartment in a creative community
Archetype: The Creative Innovator
Goals: Build an impressive portfolio, attract diverse clients, and maintain creative freedom
Challenges: Inconsistent income, self-promotion struggles, and managing multiple projects
Fears: Creative burnout and economic instability in the freelance market
Problems: Finding a steady flow of reliable clients and meeting tight deadlines
Values: Creativity, authenticity, and flexibility
Buying Decision Process: Decisions are heavily influenced by design aesthetics and functionality; seeks online reviews and values peer recommendations
Internet & Website Usage: Spends significant time on portfolio sites (like Behance), social media for creative inspiration, and freelance job boards

6. Carlos – The Aspiring Entrepreneur
Age: 38
Gender: Male
Job: Startup Founder in the tech industry
Education: MBA from a reputable institution
Location: Urban hub (e.g., San Francisco Bay Area)
Family Situation: Married with one young child
Archetype: The Visionary Leader
Goals: Scale his business, disrupt his market, and establish a strong brand identity
Challenges: Securing funding, managing rapid team growth, and navigating stiff market competition
Fears: Business failure and the risk of market downturns impacting his startup
Problems: Balancing aggressive growth with sustainable practices and managing cash flow effectively
Values: Innovation, calculated risk-taking, and perseverance
Buying Decision Process: Data-driven, he carefully compares ROI, reads case studies, and values expert insights and peer endorsements
Internet & Website Usage: Frequently visits business news platforms, startup forums, and professional networks to gather insights and track market trends

7. Lisa – The Dedicated Stay-at-Home Parent
Age: 36
Gender: Female
Job: Full-time parent
Education: Associate degree
Location: Suburban community (e.g., a family-friendly neighborhood in Ohio)
Family Situation: Married with two young children
Archetype: The Nurturer
Goals: Create a supportive home environment, manage household responsibilities efficiently, and pursue personal interests when possible
Challenges: Balancing childcare with personal time, managing a tight household budget, and combating feelings of isolation
Fears: Failing to meet her children’s needs or unexpected financial emergencies
Problems: Time management struggles and feeling overwhelmed by daily responsibilities
Values: Family, community, and practicality
Buying Decision Process: Diligently researches products online, values affordability and reliability, and trusts recommendations from parenting communities and online reviews
Internet & Website Usage: Regularly visits parenting blogs, participates in online forums (like Facebook groups), and shops online for household and family products

8. Brandon – The Practical Blue-Collar Worker
Age: 32
Gender: Male
Job: Construction Worker
Education: High school diploma with vocational training
Location: Industrial city in the Midwest
Family Situation: Married with one child
Archetype: The Hands-On Doer
Goals: Provide financial stability for his family, improve his skill set, and invest in quality tools and equipment
Challenges: Long and physically demanding work hours, managing family time, and limited opportunities for upward mobility
Fears: Workplace injuries and economic downturns affecting job security
Problems: Fatigue from physically demanding work and limited time for personal pursuits
Values: Hard work, reliability, and practical solutions
Buying Decision Process: Prefers products known for durability and functionality; bases decisions on brand reputation, clear product details, and price comparisons
Internet & Website Usage: Uses websites for practical research (tool reviews, local job listings), basic social media (often Facebook), and online shopping for work or home improvement items

9. Katie – The Independent Remote Worker
Age: 28
Gender: Female
Job: Remote Customer Service Representative
Education: Bachelor’s degree in Communications
Location: Rural setting (e.g., a small town in Vermont)
Family Situation: Single, living independently
Archetype: The Self-Reliant Individual
Goals: Build a sustainable work-life balance, further her career from a remote setting, and enjoy personal freedom
Challenges: Limited local networking opportunities, occasional connectivity issues, and feelings of isolation
Fears: Career stagnation and missing out on urban professional opportunities
Problems: Navigating professional growth without a traditional office environment and overcoming digital isolation
Values: Independence, flexibility, and community connection—even if virtual
Buying Decision Process: Researches extensively online, values detailed information and honest reviews, and carefully weighs cost-effectiveness and long-term benefits
Internet & Website Usage: Relies heavily on remote work tools (video conferencing, project management apps), participates in online professional communities, and accesses digital courses for self-improvement

10. Sean – The Dedicated Academic Researcher
Age: 55
Gender: Male
Job: University Professor and Researcher
Education: Ph.D. in his field of expertise
Location: College town in the Northeast U.S.
Family Situation: Married with adult children
Archetype: The Intellectual
Goals: Advance scholarly research, mentor students, and contribute to his academic community through publications
Challenges: Balancing teaching duties with extensive research, navigating grant applications, and adapting to evolving academic technologies
Fears: Falling behind in his field due to rapid changes, funding cuts, and rejection of his work in peer reviews
Problems: Time management between administrative tasks and research, bureaucratic hurdles, and adapting to new digital tools
Values: Knowledge, intellectual integrity, and academic rigor
Buying Decision Process: Makes decisions based on detailed product specifications, peer-reviewed studies, and long-term academic value; relies on expert opinions and academic endorsements
Internet & Website Usage: Regularly accesses academic databases, professional journals, educational platforms, and academic networking sites (such as ResearchGate and LinkedIn) for research and collaboration
'''
    # Process each PNG file separately.
    for i, file_path in enumerate(file_paths, start=1):
        try:
            image = PIL.Image.open(file_path)
            print(f"Accessed '{file_path}' successfully.")
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            continue
        except PIL.UnidentifiedImageError:
            print(f"Error: {file_path} is not a valid image file.")
            continue
        except Exception as e:
            print(f"An unexpected error occurred while processing {file_path}: {e}")
            continue

        response_obj = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[text_example, image],
        )
        print(f"Response for file {i} received successfully.")
        text_data = response_obj.text

        # Group rows by product.
        products_dict = {}  # Key: product name, Value: list of rows.
        
        for line in text_data.split("\n"):
            line = line.strip()
            if not line:
                continue

            # Split line on pipe.
            parts = line.split("|")
            # Check if we have the expected 6 parts.
            if len(parts) == 6:
                processed_parts = []
                for part in parts:
                    if ":" in part:
                        # Split only on the first occurrence.
                        key, value = part.split(":", 1)
                        processed_parts.append(value.strip())
                    else:
                        processed_parts.append(part.strip())
            elif len(parts) == 5:
                # Attempt to recover missing field:
                # The first part might include both Name and Product, separated by a colon.
                first_part = parts[0].strip()
                first_split = first_part.split(":", 1)
                if len(first_split) == 2:
                    # Create two parts: one for Name and one for Product.
                    name_val = first_split[0].strip()
                    product_val = first_split[1].strip()
                    processed_parts = [name_val, product_val]
                    # Process the remaining 4 parts.
                    for part in parts[1:]:
                        if ":" in part:
                            key, value = part.split(":", 1)
                            processed_parts.append(value.strip())
                        else:
                            processed_parts.append(part.strip())
                else:
                    print(f"Warning: Cannot split first part correctly: {line}")
                    continue
            else:
                print(f"Warning: Line does not have 5 or 6 parts and will be skipped: {line}")
                continue

            # Validate that we now have exactly 6 columns.
            if len(processed_parts) != 6:
                print(f"Warning: Processed line does not have 6 columns and will be skipped: {processed_parts}")
                continue

            # Group by product (second field)
            product = processed_parts[1]
            if product not in products_dict:
                products_dict[product] = []
            products_dict[product].append(processed_parts)

        # Write one CSV file per product.
        for product, rows in products_dict.items():
            sanitized_product = sanitize_filename(product)
            csv_filename = os.path.join(csv_folder, f'reviews_{i}_{sanitized_product}.csv')
            try:
                with open(csv_filename, mode="w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    # Write header as specified.
                    writer.writerow(["Name", "Product", "Score", "Price", "Design", "Reason"])
                    writer.writerows(rows)
                print(f"CSV file '{csv_filename}' created successfully with {len(rows)} row(s).")
            except Exception as e:
                print(f"Failed to write CSV file '{csv_filename}': {e}")
    
    # Define the folder containing CSV files
    folder_path = csv_folder
    output_file = os.path.join(csv_folder, 'master.csv')

    # Initialize a list to store summary data
    summary_data = []

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the file is a CSV
        if filename.endswith('.csv'):
            try:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)
                
                # Calculate required metrics
                total_score = df['Score'].sum()
                scores_above_80 = df[df['Score'] >= 80].shape[0]
                scores_65_to_79 = df[(df['Score'] >= 65) & (df['Score'] < 80)].shape[0]
                scores_below_80 = df[df['Score'] < 80].shape[0]
                avg_price = df['Price'].mean()
                avg_design = df['Design'].mean()
                
                # Append results to summary data
                summary_data.append([
                    filename, total_score, scores_above_80, scores_65_to_79,
                    scores_below_80, avg_price, avg_design
                ])
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Create a DataFrame for the master CSV
    columns = [
        'Filename', 'Total Score', 'Scores >= 80', 'Scores 65-79',
        'Scores < 80', 'Average Price', 'Average Design'
    ]
    master_df = pd.DataFrame(summary_data, columns=columns)

    # Save the master CSV
    master_df.to_csv(output_file, index=False)
    print(f"Master CSV saved as {output_file}")
