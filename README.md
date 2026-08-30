# Pass-pwned: Password Analysis Using the RockYou Subset

Independent academic research investigating whether common password-strength checkers detect sequential and pattern-based weaknesses in real-world passwords and where they fall short.       

**Status:** Manuscript currently in the academic publication process. Full methodology, dataset details, and results are withheld from this repository until publication concludes. This README summarizes scope and approach only.        

----------
### Overview
Password strength meters (PSMs) are widely deployed but rarely validated against real leaked-password data at scale. This project evaluates several classes of strength-estimation approaches against a subset of the RockYou leaked password corpus, focusing specifically on their ability to catch sequential patterns (e.g., keyboard walks, incrementing digits) that are trivially guessable but often scored as "strong."       

### Research Questions      
Do popular password-strength models flag sequential patterns as weak, or do they systematically miss them?        
How much does detection accuracy vary across model types (entropy-based, ML-based, regex/rule-based)?             
Where is the practical blind spot for real-world PSM deployments?               

### Approach            
1. Curated a subset of ~10,000 passwords from the RockYou leak for controlled analysis within an isolated environment                
2. Benchmarked four strength-estimation approaches: entropy-based scoring, zxcvbn, regex/rule-based sequential detection, and a human-generated baseline       
3. Compared detection rates and false-positive/false-negative behaviour across models      
4. Full parameter choices, code, and quantitative results are not published here pending the outcome of the submission process.
   Reach out via the contact inf obelow if you'd like more detail for academic or evaluation purposes.        

### Repository Contents        
/data          → sample/early dataset used for exploratory analysis
​

-------------

***Advisor***       
This research was conducted under the guidance of Professor Dr. Nirali H. Gondaliya, HoD Physics at SVMIT-Bharuch.                 
***Contact***          
For inquiries about this research (academic collaboration, evaluation, etc.), reach out at [Email](sneha.patel.infosec@gmail.com) or via [LinkedIn](https://www.linkedin.com/in/sneha-patel-infosec/).                     
***Citation***             
A citation will be added here once the manuscript is accepted/published. If referencing this work in the interim, please contact the author directly.                    

