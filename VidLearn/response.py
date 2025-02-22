from google import genai
from google.genai import types

import PIL.Image

image = PIL.Image.open('/insert/image/path.png')

client = genai.Client(api_key="INSERT_API_KEY")
text_example = '''
For each of the people above, assume they are checking the website. the website's landing page image is attached. make them rate the website out of 100, and tell me things theyd like and not like about it, basically AB testing, and this is one of the tested websites.
remove any unnecessary text, any addition text other than what i am going to give you should be removed. only give one line per person and no other text. and here's exactly how your output should be generated: 
Name: X, Score: X, Likes: X, Dislikes: X

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
response = client.models.generate_content(

    model="gemini-2.0-flash",
    # model="gemini-1.5-flash-8b-exp-0827",
    contents=[text_example, image])

print(response.text)
