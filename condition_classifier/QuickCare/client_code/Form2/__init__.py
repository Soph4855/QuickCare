from ._anvil_designer import Form2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    global features
    features = [0] * 132
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    condition_prediction = (anvil.server.call('predict_condition', features))[0]
    if condition_prediction:
      self.label_2.visible = True
      if (str(condition_prediction) == 'Fungal infection'):
        self.label_2.text = "You may be experiencing a fungal infection.\n\nA fungal infection is a type of infection caused by fungi, which can affect various parts of the body, such as the skin, nails, or internal organs. Treatment typically involves the use of antifungal medications, either applied topically or taken orally, depending on the location and severity of the infection. In some cases, specialized treatments like antifungal shampoos for scalp infections or nail lacquers for nail infections may be necessary, and in severe systemic infections, antifungal injections or a combination of therapies may be prescribed under medical supervision." 
      if (str(condition_prediction) == 'Allergy'):
        self.label_2.text = "You may be experiencing an allergy.\n\nAn allergy is an exaggerated immune response to a specific substance or allergen, resulting in symptoms such as sneezing, itching, or difficulty breathing. Treatment often involves avoiding the allergen, using medications to manage symptoms, and in some cases, immunotherapy may be recommended for long-term relief."
      if (str(condition_prediction) == 'GERD'):
        self.label_2.text = "You may be experiencing GERD.\n\nGERD, or Gastroesophageal Reflux Disease, is a chronic condition characterized by the backward flow of stomach acid into the esophagus, causing symptoms such as heartburn and regurgitation; treatment typically involves lifestyle modifications, medication to reduce stomach acid production, and in some cases, surgical interventions may be considered to alleviate symptoms and prevent complications."
      if (str(condition_prediction) == 'Chronic cholestasis'):
        self.label_2.text = "You may be experiencing chronic cholestasis.\n\nChronic cholestasis is a condition characterized by the impaired flow of bile from the liver, leading to a buildup of bile acids and other substances in the liver and bloodstream, often resulting in symptoms such as jaundice, itching, and fatigue. Treatment primarily involves addressing the underlying cause of cholestasis, managing symptoms with medications such as ursodeoxycholic acid to promote bile flow and relieve itching, and in severe cases, liver transplantation may be necessary to restore proper liver function and alleviate complications associated with chronic cholestasis."
      if (str(condition_prediction) == 'Drug Reaction'):
        self.label_2.text = "You may be experiencing a drug reaction.\n\nA drug reaction refers to a response or unwanted side effect that occurs after taking a medication, which can vary in severity from mild discomfort to life-threatening conditions. Treatment for drug reactions typically involves discontinuing the offending drug, supportive care to alleviate symptoms and manage complications, and in some cases, using specific medications, such as antihistamines, corticosteroids, or epinephrine, to address allergic or severe reactions, while closely monitoring the patient's condition and providing appropriate medical intervention as necessary."
      if (str(condition_prediction) == 'Peptic ulcer diseae'):
        self.label_2.text = "You may be experiencing peptic ulcer disease.\n\nPeptic ulcer disease is a condition characterized by open sores or ulcers that develop on the lining of the stomach or upper part of the small intestine, often causing abdominal pain and discomfort. Treatment for peptic ulcer disease typically involves a combination of medications to reduce stomach acid production, antibiotics to eradicate the presence of H. pylori bacteria (a common cause of ulcers), and lifestyle modifications such as avoiding irritants like tobacco and certain medications, as well as adopting a healthy diet to promote healing and prevent ulcer recurrence. In some cases, endoscopic procedures or surgery may be necessary to address complications or refractory ulcers that do not respond to initial treatment."
      if (str(condition_prediction) == 'AIDS'):
        self.label_2.text = "You may be experiencing AIDS.\n\nAIDS, or Acquired Immunodeficiency Syndrome, is a chronic and advanced stage of HIV (Human Immunodeficiency Virus) infection, characterized by severe damage to the immune system, leaving the body vulnerable to opportunistic infections and certain cancers; treatment for AIDS typically involves a combination of antiretroviral therapy (ART) consisting of multiple medications that suppress the replication of the HIV virus, as well as supportive care to manage opportunistic infections, prevent complications, and improve overall quality of life. Strict adherence to ART and regular medical monitoring are crucial for effective management of AIDS and to maintain the immune system's function."
      if (str(condition_prediction) == 'Diabetes '):
        self.label_2.text = "You may be experiencing diabetes.\n\nDiabetes is a chronic metabolic disorder characterized by high blood sugar levels due to either insufficient insulin production (Type 1) or ineffective use of insulin (Type 2), leading to various complications. Treatment for diabetes typically involves lifestyle modifications such as adopting a healthy diet, regular exercise, monitoring blood sugar levels, and taking medication (including insulin injections or oral antidiabetic drugs) to regulate blood sugar levels, along with regular medical check-ups to manage the condition, prevent complications, and maintain overall well-being. In addition, diabetes management often includes education and support to help individuals make informed decisions about their health, self-care practices, and long-term management strategies."
      if (str(condition_prediction) == 'Gastroenteritis'):
        self.label_2.text = "You may be experiencing gastroenteritis.\n\nGastroenteritis is an inflammation of the stomach and intestines, typically caused by viral or bacterial infections, leading to symptoms like diarrhea, vomiting, abdominal pain, and nausea; treatment for gastroenteritis mainly focuses on rehydration to replace lost fluids and electrolytes through oral rehydration solutions, drinking clear fluids, and, in severe cases, intravenous fluids may be necessary, along with supportive care such as rest, dietary adjustments, and medication to manage symptoms like antiemetics for vomiting or antidiarrheal agents under medical supervision to alleviate discomfort and aid in recovery."
      if (str(condition_prediction) == 'Bronchial Asthma'):
        self.label_2.text = "You may be experiencing bronchial asthma.\n\nBronchial asthma is a chronic respiratory condition characterized by inflammation and narrowing of the airways, leading to recurrent episodes of wheezing, shortness of breath, coughing, and chest tightness. Treatment for bronchial asthma typically involves a combination of long-term control medications such as inhaled corticosteroids or bronchodilators to reduce airway inflammation and improve airflow, as well as rescue medications like short-acting bronchodilators to provide immediate relief during asthma attacks. It is also recommended that patients identify and avoid triggers, adopt proper inhaler technique, and create an asthma action plan with healthcare professionals to effectively manage symptoms, prevent exacerbations, and improve overall respiratory function."
      if (str(condition_prediction) == 'Hypertension '):
        self.label_2.text = "You may be experiencing hypertension.\n\nHypertension, also known as high blood pressure, is a medical condition characterized by elevated pressure in the arteries, which can increase the risk of heart disease, stroke, and other health complications. Treatment for hypertension typically involves lifestyle modifications, such as adopting a healthy diet (low in sodium and high in fruits and vegetables), regular physical activity, weight management, reducing alcohol consumption, and quitting smoking, along with medication management, as prescribed by a healthcare professional, which may include various classes of antihypertensive drugs like diuretics, beta-blockers, ACE inhibitors, angiotensin receptor blockers (ARBs), calcium channel blockers, or other medications to lower blood pressure effectively and prevent associated complications. Regular blood pressure monitoring and adherence to the treatment plan are essential in controlling hypertension and promoting cardiovascular health."
      if (str(condition_prediction) == 'Migraine'):
        self.label_2.text = "You may be experiencing a migraine.\n\nA migraine is a severe headache often accompanied by other symptoms such as nausea, sensitivity to light and sound, and visual disturbances. The treatment for migraines typically involves a combination of acute and preventive measures. Acute treatments aim to relieve the pain and associated symptoms during a migraine attack and may include over-the-counter pain relievers like ibuprofen or prescription medications such as triptans or ergot derivatives. Anti-nausea medications may also be prescribed to alleviate nausea and vomiting. Preventive treatments are used for individuals who experience frequent or severe migraines. These medications, such as beta-blockers, antiepileptic drugs, calcium channel blockers, or antidepressants, are taken regularly to reduce the frequency and intensity of migraine attacks. Lifestyle modifications, including stress management, regular sleep patterns, and dietary changes, can also be beneficial in preventing migraines. It's important for individuals with migraines to work closely with their healthcare provider to develop a personalized treatment plan tailored to their specific needs."
      if (str(condition_prediction) == 'Cervical spondylosis'):
        self.label_2.text = "You may be experiencing cervical spondylosis.\n\nCervical spondylosis is a degenerative condition that affects the discs and joints of the neck, leading to neck pain, stiffness, and potential nerve compression. The treatment for cervical spondylosis focuses on managing symptoms and preventing further progression. Conservative treatment options include rest, physical therapy, neck exercises to improve strength and flexibility, pain medication, and the use of neck braces or collars to provide support. Heat or cold therapy, traction, and massage can also help alleviate symptoms. In more severe cases or when conservative measures are ineffective, interventions such as epidural steroid injections may be considered for pain relief. Surgery may be recommended in rare cases where nerve compression causes severe and persistent symptoms or neurological deficits. It's essential to consult with a healthcare professional to determine the most appropriate treatment approach based on the severity of symptoms and individual needs."
      if (str(condition_prediction) == 'Paralysis (brain hemorrhage)'):
        self.label_2.text = "You may be experiencing paralysis, potentially caused by a brain hemorrhage.\n\nParalysis is the loss of muscle function and voluntary movement in a part of the body, often caused by damage to the nerves or spinal cord. The treatment for paralysis varies depending on the underlying cause and the extent of paralysis. In cases of temporary paralysis, such as that caused by nerve compression or inflammation, addressing the underlying condition may lead to improvement or full recovery. Physical therapy is often a crucial aspect of paralysis treatment, as it helps maintain muscle strength, prevent muscle atrophy, and improve mobility. Occupational therapy is also beneficial for teaching adaptive techniques to perform daily activities. For permanent paralysis resulting from spinal cord injuries or certain neurological conditions, there is no cure, but rehabilitation, assistive devices (such as wheelchairs), and various adaptive strategies can greatly enhance the individual's quality of life and independence. Additionally, ongoing medical care and management are essential to prevent complications such as pressure sores, respiratory issues, and joint contractures. Researchers continue to explore various avenues, including regenerative medicine and neural prosthetics, for potential future treatments to restore function in paralyzed individuals."
      if (str(condition_prediction) == 'Jaundice'):
        self.label_2.text = "You may be experiencing jaundice.\n\nJaundice is a medical condition characterized by the yellowing of the skin and eyes, resulting from an accumulation of bilirubin in the bloodstream. The treatment for jaundice primarily depends on the underlying cause. In cases of mild jaundice caused by conditions like viral infections or medications, treatment may involve addressing the root cause, providing supportive care, and ensuring adequate hydration. For more severe jaundice caused by liver or bile duct disorders, medical interventions may include specific medications to treat the underlying condition, phototherapy (exposure to special lights that help break down excess bilirubin), and in some cases, blood transfusions or surgery to manage complications. It is crucial to seek immediate medical attention for jaundice, as it can indicate serious underlying health issues that require proper diagnosis and management."
      if (str(condition_prediction) == 'Malaria'):
        self.label_2.text = "You may be experiencing malaria.\n\nMalaria is a mosquito-borne infectious disease caused by parasites of the Plasmodium species, leading to symptoms such as fever, chills, and flu-like illness. The treatment for malaria involves the use of antimalarial medications to eliminate the parasites from the bloodstream. The choice of medication depends on the species of Plasmodium causing the infection and the region's drug resistance patterns. Commonly used antimalarial drugs include chloroquine, artemisinin-based combination therapies (ACTs), mefloquine, and doxycycline. In severe cases of malaria or when the infection is caused by drug-resistant strains, intravenous antimalarial drugs like quinine or artesunate may be used in a hospital setting. Early and effective treatment is essential to prevent complications and ensure a complete recovery from malaria. Additionally, preventive measures such as the use of insecticide-treated bed nets and taking prophylactic antimalarial medication are crucial for individuals living in or traveling to areas where malaria is endemic."
      if (str(condition_prediction) == 'Chicken pox'):
        self.label_2.text = "You may be experiencing chicken pox.\n\nChickenpox is a highly contagious viral infection caused by the varicella-zoster virus, characterized by an itchy rash with small, red spots that eventually form fluid-filled blisters. The treatment for chickenpox mainly focuses on managing the symptoms and promoting comfort during the course of the infection. Over-the-counter pain relievers like acetaminophen or ibuprofen can help reduce fever and relieve discomfort. Calamine lotion or colloidal oatmeal baths may be used to soothe the itching and dry out the blisters. It is essential to avoid scratching the blisters to prevent infection and scarring. In some cases, antiviral medications may be prescribed for high-risk individuals or those with severe symptoms, but generally, chickenpox is a self-limiting condition that resolves on its own within a few weeks. It's important to keep the affected person isolated to prevent the spread of the virus to others, especially those who are susceptible to complications, such as pregnant women, newborns, and individuals with weakened immune systems. Vaccination against chickenpox is highly effective in preventing the infection and its complications and is recommended as part of routine childhood immunization."
      if (str(condition_prediction) == 'Dengue'):
        self.label_2.text = "You may be experiencing dengue.\n\nDengue is a mosquito-borne viral infection caused by the dengue virus, characterized by flu-like symptoms and, in severe cases, potentially life-threatening complications like dengue hemorrhagic fever or dengue shock syndrome. There is no specific antiviral treatment for dengue, so the focus of treatment is on managing symptoms and preventing complications. People with dengue are advised to stay well-hydrated by drinking plenty of fluids to avoid dehydration. Pain relievers such as acetaminophen (paracetamol) are used to reduce fever and alleviate pain. Nonsteroidal anti-inflammatory drugs (NSAIDs) like aspirin should be avoided as they can increase the risk of bleeding in dengue. In severe cases, hospitalization may be necessary, and supportive care, such as intravenous fluids, blood transfusions, and close monitoring of vital signs, may be provided to manage complications and improve outcomes. Early detection and prompt medical attention are crucial for timely intervention and reducing the risk of severe dengue-related complications. Prevention efforts, such as vector control measures to reduce mosquito breeding sites and the use of protective clothing and insect repellents, are also essential in preventing dengue transmission."
      if (str(condition_prediction) == 'Typhoid'):
        self.label_2.text = "You may be experiencing typhoid.\n\nTyphoid is a bacterial infection caused by Salmonella typhi, typically transmitted through contaminated food and water, and characterized by symptoms such as prolonged fever, headache, abdominal pain, and gastrointestinal disturbances. The treatment for typhoid involves the use of antibiotics to eliminate the Salmonella bacteria from the body. Commonly prescribed antibiotics for typhoid include ciprofloxacin, ceftriaxone, and azithromycin. It is essential to complete the full course of antibiotics as prescribed by a healthcare professional to ensure complete eradication of the bacteria and prevent the development of antibiotic-resistant strains. Additionally, supportive care, such as maintaining adequate hydration with oral rehydration solutions or intravenous fluids if necessary, rest, and a nutritious diet, can help in recovery and alleviating symptoms. Preventive measures, such as practicing good hygiene, drinking clean and safe water, and avoiding consuming raw or undercooked food, can reduce the risk of contracting typhoid. Vaccination against typhoid is also available and recommended for travelers to areas where the disease is prevalent or for individuals at higher risk of exposure."
      if (str(condition_prediction) == 'hepatitis A'):
        self.label_2.text = "You may be experiencing hepatitis A.\n\nHepatitis A is a viral liver infection caused by the hepatitis A virus (HAV) and is typically transmitted through contaminated food or water. There is no specific treatment for hepatitis A, as the infection typically resolves on its own without causing long-term liver damage. Supportive care is essential, which includes rest, staying well-hydrated, and avoiding alcohol and certain medications that may further stress the liver. In most cases, individuals with hepatitis A recover within a few weeks to a few months. However, it's essential to seek medical attention for proper diagnosis and monitoring, especially for individuals with severe symptoms or those at higher risk of complications, such as pregnant women or individuals with pre-existing liver conditions. Prevention is crucial for hepatitis A, and vaccination is available and recommended, especially for travelers to areas with high hepatitis A prevalence or for individuals at increased risk of exposure due to certain occupations or activities. Good hygiene practices, such as handwashing and consuming clean and safe food and water, can also help prevent the spread of hepatitis A."
      if (str(condition_prediction) == 'Hepatitis B'):
        self.label_2.text = "You may be experiencing hepatitis B.\n\nHepatitis B is a viral liver infection caused by the hepatitis B virus (HBV) and can range from acute illness to a chronic condition, potentially leading to severe liver damage and complications. The treatment for hepatitis B aims to control the virus, manage symptoms, and prevent liver-related complications. For acute hepatitis B, supportive care such as rest, staying hydrated, and avoiding alcohol is often sufficient, as the body's immune system can clear the infection in most cases. However, for chronic hepatitis B, antiviral medications such as entecavir, tenofovir, lamivudine, adefovir, or interferon may be prescribed to suppress viral replication and reduce liver inflammation. These medications can help slow down the progression of the disease, lower the risk of liver damage, and improve long-term outcomes. Regular monitoring of liver function and HBV viral load is essential to assess the effectiveness of treatment and adjust the medications if needed. In some cases, a combination of antiviral medications may be used, and treatment may be lifelong, especially for individuals at a high risk of developing complications. It's essential for individuals with chronic hepatitis B to work closely with healthcare professionals to manage the condition effectively and prevent complications such as cirrhosis or liver cancer. Vaccination against hepatitis B is also available and highly effective in preventing new infections and is recommended for all individuals, especially those at higher risk of exposure to HBV."
      if (str(condition_prediction) == 'Hepatitis C'):
        self.label_2.text = "You may be experiencing hepatits C.\n\nHepatitis C is a viral liver infection caused by the hepatitis C virus (HCV), and it can lead to chronic liver disease if left untreated. The treatment for hepatitis C has evolved significantly over the years, and the current standard of care involves the use of direct-acting antiviral (DAA) medications. These medications target specific steps in the HCV replication process and have a high cure rate, often reaching over 95%. The treatment duration varies depending on the specific DAA regimen used and the type of HCV genotype, but most treatment courses last for 8 to 12 weeks. Regular monitoring of liver function and viral load during and after treatment is essential to assess the effectiveness of therapy and ensure successful clearance of the virus. Successful treatment of hepatitis C can lead to a sustained virologic response (SVR), which means the virus is undetectable in the blood for at least 12 weeks after completing treatment, indicating a cure and significantly reducing the risk of liver-related complications. Early diagnosis, access to appropriate medical care, and adherence to the prescribed treatment plan are crucial for achieving successful outcomes in individuals with hepatitis C."
      if (str(condition_prediction) == 'Hepatitis D'):
        self.label_2.text = "You may be experiencing hepatitis D.\n\nHepatitis D, also known as delta hepatitis, is a viral liver infection caused by the hepatitis D virus (HDV), which can only occur in individuals already infected with hepatitis B. The treatment for hepatitis D is challenging, as there is no specific antiviral therapy available for HDV. Since HDV requires the presence of hepatitis B to replicate, the primary approach is to target hepatitis B with antiviral medications like entecavir or tenofovir, which can help suppress HBV replication and slow down HDV's progression. In some cases, interferon alpha may be used to treat hepatitis D, as it has shown some efficacy in reducing HDV viral load and liver inflammation. Liver transplantation may be considered for individuals with severe liver damage due to chronic hepatitis D and B co-infection. Preventing hepatitis B through vaccination is essential to avoid hepatitis D infection, as HDV can only infect individuals who are already hepatitis B carriers."
      if (str(condition_prediction) == 'Hepatitis E'):
        self.label_2.text = "You may be experiencing hepatitis E.\n\nHepatitis E is a viral liver infection caused by the hepatitis E virus (HEV), commonly transmitted through contaminated water and food in areas with poor sanitation. The treatment for hepatitis E is typically supportive, as most cases of acute hepatitis E resolve on their own without the need for specific antiviral therapy. Rest, maintaining adequate hydration, and avoiding alcohol are important aspects of supportive care. In most cases, individuals with acute hepatitis E recover completely within a few weeks to months. However, pregnant women and individuals with pre-existing liver conditions are at higher risk of developing severe hepatitis E, and they may require closer monitoring and medical attention. There is currently no approved specific antiviral medication for treating hepatitis E, but research is ongoing to develop effective treatments for those with chronic or severe cases. Preventive measures, such as drinking clean and safe water, practicing good hygiene, and avoiding undercooked or contaminated food, are crucial to reduce the risk of hepatitis E infection."
      if (str(condition_prediction) == 'Alcoholic hepatitis'):
        self.label_2.text = "You may be experiencing alcoholic hepatitis.\n\nAlcoholic hepatitis is a liver condition characterized by inflammation and damage to the liver due to excessive and prolonged alcohol consumption. The treatment for alcoholic hepatitis involves a combination of medical interventions and lifestyle changes. The first and most crucial step is to completely stop drinking alcohol to prevent further damage to the liver. Nutritional support is vital, and individuals may receive supplements or a special diet to correct deficiencies and improve liver function. Medications like corticosteroids or pentoxifylline may be prescribed to reduce inflammation in the liver. In severe cases, hospitalization may be necessary, and in some instances, a liver transplant might be considered for those with end-stage liver disease and liver failure. It is essential to seek medical attention promptly for proper evaluation and management of alcoholic hepatitis to improve the chances of recovery and prevent complications. Additionally, addressing any underlying alcohol use disorder through counseling or rehabilitation programs is essential to maintain long-term liver health and overall well-being."
      if (str(condition_prediction) == 'Tuberculosis'):
        self.label_2.text = "You may be experiencing tuberculosis.\n\nTuberculosis (TB) is a bacterial infection caused by Mycobacterium tuberculosis, primarily affecting the lungs but can also affect other parts of the body. The treatment for tuberculosis typically involves a combination of multiple antibiotics, known as anti-tuberculosis drugs, to ensure effective eradication of the bacteria and prevent the development of drug-resistant strains. The most common first-line drugs used in TB treatment are isoniazid, rifampin, ethambutol, and pyrazinamide. The treatment duration for drug-susceptible TB usually lasts for at least six months and may extend to nine months or more depending on the specific regimen and the patient's response to treatment. It is crucial for individuals with TB to adhere strictly to the prescribed treatment regimen and attend regular medical check-ups to monitor progress and ensure successful treatment completion. Additionally, for drug-resistant TB cases, more complex and prolonged treatment regimens with second-line medications may be necessary, and management should be conducted under the supervision of experienced healthcare professionals. Contact tracing and preventive treatment for individuals at high risk of TB infection, such as close contacts of infected individuals or those with compromised immune systems, are also important strategies to control the spread of the disease."
      if (str(condition_prediction) == 'Common Cold'):
        self.label_2.text = "You may be experiencing the common cold.\n\nThe common cold is a viral infection of the upper respiratory tract, characterized by symptoms such as a runny or stuffy nose, sneezing, sore throat, and cough. Treatment for the common cold primarily focuses on managing symptoms to alleviate discomfort. Over-the-counter medications, such as decongestants, antihistamines, and pain relievers (e.g., acetaminophen or ibuprofen), can help relieve nasal congestion, reduce inflammation, and alleviate headache or body aches. Drinking plenty of fluids and staying hydrated is essential to help loosen mucus and soothe a sore throat. Resting and getting enough sleep are crucial for allowing the body to fight off the viral infection and recover more quickly. Gargling with warm saltwater can help soothe a sore throat. Using a humidifier or taking steam inhalation can also ease nasal congestion and provide relief from dry air. It's important to note that antibiotics are not effective against the common cold since it is a viral infection, and unnecessary use of antibiotics can contribute to antibiotic resistance. Most cases of the common cold resolve on their own within a week or two, but if symptoms worsen or persist, or if there are signs of a secondary bacterial infection, it's advisable to consult a healthcare professional for further evaluation and management."
      if (str(condition_prediction) == 'Pneumonia'):
        self.label_2.text = "You may be experiencing pneumonia.\n\nPneumonia is a respiratory infection that causes inflammation in the air sacs of the lungs, leading to symptoms such as cough, difficulty breathing, fever, and chest pain. The treatment for pneumonia depends on the underlying cause and the severity of the infection. In most cases of bacterial pneumonia, antibiotics are prescribed to target the specific bacteria causing the infection. It's essential to take the full course of antibiotics as prescribed by a healthcare professional to ensure complete eradication of the bacteria and prevent the development of antibiotic-resistant strains. In cases of viral pneumonia, antiviral medications may be used if the infection is caused by a specific virus, such as influenza. Supportive care is crucial for pneumonia treatment, which may include rest, staying well-hydrated, using a humidifier or taking steam inhalation to ease breathing, and managing fever and discomfort with over-the-counter pain relievers and antipyretics. In severe cases or when complications arise, hospitalization may be necessary, and oxygen therapy or mechanical ventilation might be required to support breathing. It's essential to seek medical attention promptly if symptoms of pneumonia develop, especially in high-risk individuals, such as the elderly, young children, or those with underlying health conditions, as early diagnosis and treatment can improve outcomes and prevent complications. Preventive measures, such as vaccination against certain bacterial and viral pathogens that can cause pneumonia, can also help reduce the risk of infection and its severe outcomes."
      if (str(condition_prediction) == 'Dimorphic hemmorhoids(piles)'):
        self.label_2.text = "You may be experiencing dimorphic hemmorhoids.\n\nDimorphic hemorrhoids, also known as piles, are swollen and inflamed blood vessels in the rectal and anal area, which can cause discomfort, pain, itching, and bleeding. The treatment for dimorphic hemorrhoids depends on the severity of the condition. In mild cases, self-care measures can be effective, including increasing dietary fiber intake, drinking plenty of fluids, and avoiding straining during bowel movements. Over-the-counter creams, ointments, or suppositories containing hydrocortisone or witch hazel can help alleviate symptoms like itching and inflammation. Warm sitz baths can provide relief and reduce swelling. In more severe or persistent cases, medical intervention may be necessary, and procedures like rubber band ligation, sclerotherapy, or infrared coagulation may be performed to shrink the hemorrhoids. In rare cases, surgical removal of the hemorrhoids (hemorrhoidectomy) might be considered for severe or chronic cases that do not respond to other treatments. It is essential to seek medical advice for proper diagnosis and appropriate treatment recommendations for dimorphic hemorrhoids to alleviate symptoms and prevent complications."
      if (str(condition_prediction) == 'Heart attack'):
        self.label_2.text = "You may be experiencing a heart attack. If you have reason to believe this is the case, call 9-1-1 immediately.\n\nA heart attack, also known as a myocardial infarction, occurs when blood flow to a part of the heart muscle is blocked, leading to damage or death of the heart tissue. Immediate treatment for a heart attack is critical and involves calling emergency services (911 in the United States) to seek immediate medical attention. In the hospital, treatments for a heart attack may include administering medications like aspirin to reduce blood clotting and thrombolytic drugs to dissolve blood clots in the coronary arteries. Percutaneous coronary intervention (PCI) or angioplasty may be performed to open the blocked arteries, and stents may be inserted to keep them open. Thrombectomy, a procedure to physically remove the clot, might also be used in certain cases. Cardiac rehabilitation programs are often recommended for patients after a heart attack to help them recover, improve cardiovascular health, and reduce the risk of future heart problems. Long-term management includes lifestyle changes, such as adopting a heart-healthy diet, regular exercise, quitting smoking, and taking prescribed medications, such as beta-blockers, ACE inhibitors, or statins, to manage risk factors and prevent further heart events. It's crucial for individuals at risk of a heart attack or those who have experienced one to work closely with healthcare professionals to develop a personalized treatment plan and adopt preventive measures for heart health."
      if (str(condition_prediction) == 'Varicose veins'):
        self.label_2.text = "You may have varicose veins.\n\nVaricose veins are enlarged, swollen, and twisted veins that often appear blue or dark purple, commonly found in the legs. Treatment for varicose veins aims to alleviate symptoms, improve appearance, and prevent complications. Lifestyle changes such as regular exercise, weight management, and avoiding prolonged standing or sitting can help reduce symptoms. Compression stockings may be recommended to improve blood flow and relieve discomfort. Sclerotherapy involves injecting a solution into the affected veins to collapse them and redirect blood flow to healthier veins. Endovenous laser ablation and radiofrequency ablation are minimally invasive procedures that use heat to close off and seal the varicose veins. For severe cases, surgical options such as vein stripping or ligation may be considered to remove the affected veins. It's essential to consult a healthcare professional for an evaluation and personalized treatment plan for varicose veins, as not all cases require intervention, and the best approach may vary depending on individual factors and the severity of the condition."
      if (str(condition_prediction) == 'Hypothyroidism'):
        self.label_2.text = "You may be experiencing hypothyroidism.\n\nHypothyroidism is a condition in which the thyroid gland does not produce enough thyroid hormones, leading to a slowdown of bodily functions and various symptoms. The treatment for hypothyroidism typically involves lifelong hormone replacement therapy with synthetic thyroid hormones like levothyroxine. The medication aims to restore normal thyroid hormone levels in the body and alleviate symptoms such as fatigue, weight gain, and cold intolerance. Regular monitoring of thyroid hormone levels and adjustments to the medication dosage, as needed, are essential to ensure optimal management of hypothyroidism and prevent complications associated with either undertreatment or overtreatment. It's crucial for individuals with hypothyroidism to follow their healthcare provider's guidance and maintain consistent treatment to achieve a balanced thyroid hormone level and improve overall well-being."
      if (str(condition_prediction) == 'Hyperthyroidism'):
        self.label_2.text = "You may be experiencing hyperthyroidism.\n\nHyperthyroidism is a condition that involves the thyroid gland producing an excessive amount of thyroid hormones. Drugs like Methimazole or Propylthiouracil (PTU) can help reduce thyroid hormone production and are commonly used in cases of Graves' disease. Additionally, medications like Propranolol or Atenolol can manage symptoms like rapid heartbeat, tremors, and anxiety. Patients may also benefit from radioactive iodine therapy, a treatment that involves taking a radioactive form of iodine, which is absorbed by the thyroid gland to destroy overactive thyroid cells.Surgical removal of part or all of the thyroid gland may be necessary in some cases, especially if other treatments are not suitable or effective. Treatment choice depends on the cause and severity of symptoms as well as factors unique to the individual. Regular follow-up appointments are essential to monitor progress and ensure the best outcome. Remember, it's crucial to seek medical attention if you suspect hyperthyroidism in order to receive proper diagnosis and care."
      if (str(condition_prediction) == 'Hypoglycemia'):
        self.label_2.text = "You may be experiencing hypoglycemia.\n\nHypoglycemia is a condition characterized by low blood sugar levels, which can lead to symptoms such as shakiness, confusion, sweating, and weakness. The treatment for hypoglycemia involves raising blood sugar levels to a safe range. For individuals with diabetes, consuming fast-acting carbohydrates such as glucose tablets, fruit juice, or regular soda can quickly increase blood sugar levels. Non-diabetic individuals can also benefit from consuming sugar-containing snacks or drinks to alleviate symptoms. It is essential to follow up with a healthcare professional to identify the underlying cause of hypoglycemia and develop strategies to prevent future episodes. In some cases, adjustments to medication dosages or meal plans may be necessary to maintain stable blood sugar levels and prevent further occurrences of hypoglycemia."
      if (str(condition_prediction) == 'Osteoarthristis'):
        self.label_2.text = "You may be experiencing osteoarthritis.\n\nOsteoarthritis is a degenerative joint disease that causes the breakdown of joint cartilage and underlying bone, leading to pain, stiffness, and reduced joint function. The treatment for osteoarthritis aims to manage symptoms, improve joint function, and enhance the individual's quality of life. Non-pharmacological interventions include regular exercise, such as low-impact activities and muscle-strengthening exercises, to improve joint flexibility and support the affected joints. Weight management is crucial for reducing stress on weight-bearing joints. Physical therapy may be recommended to learn proper body mechanics and exercises to alleviate pain and maintain joint mobility. Assistive devices like canes, braces, or shoe inserts can help reduce joint strain. Pharmacological treatments for osteoarthritis include over-the-counter pain relievers like acetaminophen or nonsteroidal anti-inflammatory drugs (NSAIDs) for pain management. Topical creams or gels containing NSAIDs can also provide relief. In cases of more severe pain, prescription medications like opioids or intra-articular corticosteroid injections may be used, but their long-term use is generally avoided due to potential side effects. In some cases, hyaluronic acid injections or platelet-rich plasma (PRP) injections may be considered to provide temporary pain relief. Surgical options, such as joint realignment or joint replacement surgery, may be considered for individuals with advanced osteoarthritis and significant joint damage. A healthcare professional can help develop a comprehensive treatment plan tailored to the individual's specific needs and the severity of osteoarthritis to effectively manage symptoms and improve joint function."
      if (str(condition_prediction) == 'Arthritis'):
        self.label_2.text = "You may be experiencing arthritis.\n\nArthritis is a broad term used to describe inflammation of one or more joints, leading to pain, stiffness, and decreased joint mobility. The treatment for arthritis varies depending on the specific type and severity of the condition. Non-pharmacological interventions such as regular exercise, physical therapy, and weight management are essential in maintaining joint function and reducing pain. Hot or cold compresses, rest, and joint protection techniques may help manage symptoms. Over-the-counter pain relievers like acetaminophen or nonsteroidal anti-inflammatory drugs (NSAIDs) can provide relief for mild to moderate pain. For more severe cases or when NSAIDs are not sufficient, prescription medications like disease-modifying antirheumatic drugs (DMARDs) or biologic agents may be used to slow down the progression of certain types of inflammatory arthritis and reduce joint damage. Corticosteroid injections into the affected joint may provide short-term pain relief for some individuals. In advanced cases of arthritis that do not respond to other treatments, joint replacement surgery may be considered to improve joint function and alleviate pain. It's crucial for individuals with arthritis to work closely with healthcare professionals to develop a personalized treatment plan that includes a combination of lifestyle modifications, medications, and other interventions to effectively manage symptoms, improve joint function, and enhance overall quality of life."
      if (str(condition_prediction) == '(vertigo) Paroymsal  Positional Vertigo'):
        self.label_2.text = "You may be experiencing paroxysmal positional vertigo, or PPV.\n\nParoxysmal Positional Vertigo (PPV) is a common vestibular disorder characterized by sudden and brief episodes of intense dizziness triggered by specific head movements. The treatment for Paroxysmal Positional Vertigo typically involves a series of specific head and body maneuvers, known as canalith repositioning procedures, aimed at repositioning the displaced calcium crystals (otoconia) in the inner ear. The most well-known maneuver is the Epley maneuver. During these procedures, a healthcare professional guides the patient through a sequence of head positions to move the displaced otoconia out of the semicircular canals and into an area where they no longer cause symptoms. In most cases, the canalith repositioning procedures provide rapid relief from vertigo symptoms, and multiple treatments may be necessary to achieve complete resolution. For some individuals, additional balance exercises and vestibular rehabilitation may be recommended to further improve balance and reduce the risk of future episodes. It's essential for individuals with Paroxysmal Positional Vertigo to undergo an accurate diagnosis and receive appropriate treatment under the guidance of a healthcare professional specialized in vestibular disorders to effectively manage symptoms and prevent recurrences."
      if (str(condition_prediction) == 'Acne'):
        self.label_2.text = "You may be experiencing acne.\n\nAcne is a common skin condition characterized by the presence of pimples, blackheads, whiteheads, and other blemishes on the face, neck, chest, and back. The treatment for acne typically involves a combination of topical medications, oral medications, and lifestyle changes. Over-the-counter topical treatments containing ingredients like benzoyl peroxide, salicylic acid, or alpha hydroxy acids can help unclog pores, reduce inflammation, and control bacterial growth. Prescription-strength topical medications, such as retinoids or antibiotics, may be prescribed by a dermatologist for more severe or persistent acne. Oral antibiotics may also be used to reduce acne-causing bacteria and inflammation. For females, hormonal therapy, such as birth control pills or spironolactone, can be effective in managing hormonal acne. In cases of severe, nodular, or cystic acne, isotretinoin (Accutane) may be prescribed, but it requires close monitoring due to potential side effects. Alongside medications, adopting a gentle skincare routine, avoiding excessive face touching, and keeping the skin clean can be beneficial in managing acne. It's essential to consult a dermatologist to determine the most suitable treatment plan for specific acne concerns and receive proper guidance on acne management and prevention of scarring or skin damage."
      if (str(condition_prediction) == 'Urinary tract infection'):
        self.label_2.text = "You may be experiencing a urinary tract infection.\n\nA urinary tract infection (UTI) is a bacterial infection that can occur in any part of the urinary system, including the bladder, kidneys, ureters, and urethra. The treatment for a urinary tract infection typically involves a course of antibiotics to eliminate the bacteria causing the infection. The choice of antibiotics depends on the type of bacteria and the severity of the UTI. Commonly prescribed antibiotics for UTIs include trimethoprim-sulfamethoxazole, nitrofurantoin, and ciprofloxacin. It's essential to take the full course of antibiotics as prescribed by a healthcare professional to ensure complete eradication of the bacteria and prevent the development of antibiotic-resistant strains. In addition to antibiotics, increasing fluid intake can help flush out the bacteria from the urinary system. Pain relievers may be used to alleviate discomfort or a burning sensation during urination. For recurrent UTIs or those with complicating factors, further evaluation and management may be necessary to address underlying causes and prevent future infections. Prevention measures, such as practicing good hygiene, staying hydrated, and avoiding the use of irritating products, can help reduce the risk of developing UTIs. If symptoms of a UTI are present, it's essential to seek medical attention promptly for proper diagnosis and appropriate treatment to prevent complications and ensure a full recovery."
      if (str(condition_prediction) == 'Psoriasis'):
        self.label_2.text = "You may be experiencing psoriasis.\n\nPsoriasis is a chronic autoimmune skin condition characterized by red, scaly patches on the skin. The treatment for psoriasis aims to manage symptoms, reduce inflammation, and control the excessive skin cell growth. Topical treatments, such as corticosteroids, vitamin D analogs, and retinoids, can be applied directly to the affected areas to reduce inflammation and slow down skin cell turnover. Phototherapy, involving controlled exposure to ultraviolet light, can also help manage psoriasis by slowing down skin cell growth. For more severe or widespread psoriasis, systemic medications like methotrexate, cyclosporine, or biologic agents may be prescribed to target the underlying immune response and reduce inflammation. Combination therapies or rotational approaches may be used to optimize treatment outcomes. Lifestyle changes, such as stress management, a healthy diet, and avoiding triggers, can also help in managing psoriasis. It's essential for individuals with psoriasis to work closely with dermatologists or healthcare professionals specialized in treating skin conditions to develop a personalized treatment plan that addresses their specific needs and helps them improve their overall quality of life."
      if (str(condition_prediction) == 'Impetigo'):
        self.label_2.text = "You may be experiencing impetigo.\n\nImpetigo is a highly contagious bacterial skin infection characterized by red sores that can ooze and form a yellowish-brown crust. The treatment for impetigo typically involves topical antibiotics, such as mupirocin or fusidic acid, which are applied directly to the affected areas to eliminate the bacteria causing the infection. Keeping the affected areas clean and dry is essential to prevent further spread of the infection. In more severe or widespread cases, oral antibiotics like cephalexin or dicloxacillin may be prescribed. It's crucial to complete the full course of antibiotics as prescribed by a healthcare professional to ensure complete eradication of the bacteria and prevent recurrence or antibiotic resistance. Additionally, avoiding contact with others and practicing good hygiene, such as frequent handwashing, can help prevent the spread of impetigo to others."
        
    pass
  
  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_1.checked == True):
      features[0] = 1
    else:
      features[0] = 0
    
    pass

  def check_box_2_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_2.checked == True):
      features[1] = 1
    else:
      features[1] = 0
    
    pass

  def check_box_3_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_3.checked == True):
      features[2] = 1
    else:
      features[2] = 0
    
    pass

  def check_box_4_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_4.checked == True):
      features[3] = 1
    else:
      features[3] = 0
    
    pass

  def check_box_5_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_5.checked == True):
      features[4] = 1
    else:
      features[4] = 0
      
    pass

  def check_box_6_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_6.checked == True):
      features[5] = 1
    else:
      features[5] = 0
      
    pass

  def check_box_7_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_7.checked == True):
      features[6] = 1
    else:
      features[6] = 0
      
    pass

  def check_box_8_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_8.checked == True):
      features[7] = 1
    else:
      features[7] = 0
    
    pass

  def check_box_9_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_9.checked == True):
      features[8] = 1
    else:
      features[8] = 0
    
    pass

  def check_box_10_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_10.checked == True):
      features[9] = 1
    else:
      features[9] = 0
    
    pass

  def check_box_11_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_11.checked == True):
      features[10] = 1
    else:
      features[10] = 0
    
    pass

  def check_box_12_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_12.checked == True):
      features[11] = 1
    else:
      features[11] = 0
    
    pass

  def check_box_13_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_13.checked == True):
      features[12] = 1
    else:
      features[12] = 0
    
    pass

  def check_box_14_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_14.checked == True):
      features[13] = 1
    else:
      features[13] = 0
    
    pass

  def check_box_15_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_15.checked == True):
      features[14] = 1
    else:
      features[14] = 0
    
    pass

  def check_box_16_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_16.checked == True):
      features[15] = 1
    else:
      features[15] = 0
    
    pass

  def check_box_17_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_17.checked == True):
      features[16] = 1
    else:
      features[16] = 0
    
    pass

  def check_box_18_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_18.checked == True):
      features[17] = 1
    else:
      features[17] = 0
    
    pass

  def check_box_19_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_19.checked == True):
      features[18] = 1
    else:
      features[18] = 0
    
    pass

  def check_box_20_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_20.checked == True):
      features[19] = 1
    else:
      features[19] = 0
    
    pass

  def check_box_21_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_21.checked == True):
      features[20] = 1
    else:
      features[20] = 0
    
    pass

  def check_box_22_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_22.checked == True):
      features[21] = 1
    else:
      features[21] = 0
    
    pass
  
  def check_box_23_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_23.checked == True):
      features[22] = 1
    else:
      features[22] = 0
    
    pass

  def check_box_24_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_24.checked == True):
      features[23] = 1
    else:
      features[23] = 0
    
    pass

  def check_box_25_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_25.checked == True):
      features[24] = 1
    else:
      features[24] = 0
    
    pass

  def check_box_26_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_26.checked == True):
      features[25] = 1
    else:
      features[25] = 0
    
    pass

  def check_box_27_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_27.checked == True):
      features[26] = 1
    else:
      features[26] = 0
    
    pass

  def check_box_28_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_28.checked == True):
      features[27] = 1
    else:
      features[27] = 0
    
    pass

  def check_box_29_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_29.checked == True):
      features[28] = 1
    else:
      features[28] = 0
    
    pass

  def check_box_30_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_30.checked == True):
      features[29] = 1
    else:
      features[29] = 0
    
    pass

  def check_box_31_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_31.checked == True):
      features[30] = 1
    else:
      features[30] = 0
    
    pass

  def check_box_32_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_32.checked == True):
      features[31] = 1
    else:
      features[31] = 0
    
    pass

  def check_box_33_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_33.checked == True):
      features[32] = 1
    else:
      features[32] = 0
    
    pass

  def check_box_34_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_34.checked == True):
      features[33] = 1
    else:
      features[33] = 0
    
    pass

  def check_box_35_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_35.checked == True):
      features[34] = 1
    else:
      features[34] = 0
    
    pass

  def check_box_36_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_36.checked == True):
      features[35] = 1
    else:
      features[35] = 0
    
    pass

  def check_box_37_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_37.checked == True):
      features[36] = 1
    else:
      features[36] = 0
    
    pass

  def check_box_38_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_38.checked == True):
      features[37] = 1
    else:
      features[37] = 0
    
    pass

  def check_box_39_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_39.checked == True):
      features[38] = 1
    else:
      features[38] = 0
    
    pass

  def check_box_40_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_40.checked == True):
      features[39] = 1
    else:
      features[39] = 0
    
    pass

  def check_box_41_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_41.checked == True):
      features[40] = 1
    else:
      features[40] = 0
    
    pass

  def check_box_42_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_42.checked == True):
      features[41] = 1
    else:
      features[41] = 0
    
    pass

  def check_box_43_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_43.checked == True):
      features[42] = 1
    else:
      features[42] = 0
    
    pass

  def check_box_44_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_44.checked == True):
      features[43] = 1
    else:
      features[43] = 0
    
    pass

  def check_box_45_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_45.checked == True):
      features[44] = 1
    else:
      features[44] = 0
    
    pass

  def check_box_46_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_46.checked == True):
      features[45] = 1
      features[117] = 1
    else:
      features[45] = 0
      features[117] = 0
    
    pass

  def check_box_47_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_47.checked == True):
      features[46] = 1
    else:
      features[46] = 0
    
    pass

  def check_box_48_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_48.checked == True):
      features[47] = 1
    else:
      features[47] = 0
    
    pass

  def check_box_49_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_49.checked == True):
      features[48] = 1
    else:
      features[48] = 0
    
    pass

  def check_box_50_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_50.checked == True):
      features[49] = 1
    else:
      features[49] = 0
    
    pass

  def check_box_51_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_51.checked == True):
      features[50] = 1
    else:
      features[50] = 0
    
    pass

  def check_box_52_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_52.checked == True):
      features[51] = 1
    else:
      features[51] = 0
    
    pass

  def check_box_53_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_53.checked == True):
      features[52] = 1
    else:
      features[52] = 0
    
    pass

  def check_box_54_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_54.checked == True):
      features[53] = 1
    else:
      features[53] = 0
    
    pass

  def check_box_55_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_55.checked == True):
      features[54] = 1
    else:
      features[54] = 0
    
    pass

  def check_box_56_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_56.checked == True):
      features[55] = 1
    else:
      features[55] = 0
    
    pass

  def check_box_57_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_57.checked == True):
      features[56] = 1
    else:
      features[56] = 0
    
    pass

  def check_box_58_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_58.checked == True):
      features[57] = 1
    else:
      features[57] = 0
    
    pass

  def check_box_59_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_59.checked == True):
      features[58] = 1
    else:
      features[58] = 0
    
    pass

  def check_box_60_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_60.checked == True):
      features[59] = 1
    else:
      features[59] = 0
    
    pass

  def check_box_61_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_61.checked == True):
      features[60] = 1
    else:
      features[60] = 0
    
    pass

  def check_box_62_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_62.checked == True):
      features[61] = 1
    else:
      features[61] = 0
    
    pass

  def check_box_63_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_63.checked == True):
      features[62] = 1
    else:
      features[62] = 0
    
    pass

  def check_box_64_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_64.checked == True):
      features[63] = 1
    else:
      features[63] = 0
    
    pass

  def check_box_65_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_65.checked == True):
      features[64] = 1
    else:
      features[64] = 0
    
    pass

  def check_box_66_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_66.checked == True):
      features[65] = 1
    else:
      features[65] = 0
    
    pass

  def check_box_67_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_67.checked == True):
      features[66] = 1
    else:
      features[66] = 0
    
    pass

  def check_box_68_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_68.checked == True):
      features[67] = 1
    else:
      features[67] = 0
    
    pass

  def check_box_69_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_69.checked == True):
      features[68] = 1
    else:
      features[68] = 0
    
    pass

  def check_box_70_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_70.checked == True):
      features[69] = 1
    else:
      features[69] = 0
    
    pass

  def check_box_71_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_71.checked == True):
      features[70] = 1
    else:
      features[70] = 0
    
    pass

  def check_box_72_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_72.checked == True):
      features[71] = 1
    else:
      features[71] = 0
    
    pass

  def check_box_73_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_73.checked == True):
      features[72] = 1
    else:
      features[72] = 0
    
    pass

  def check_box_74_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_74.checked == True):
      features[73] = 1
    else:
      features[73] = 0
    
    pass

  def check_box_75_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_75.checked == True):
      features[74] = 1
    else:
      features[74] = 0
    
    pass

  def check_box_76_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_76.checked == True):
      features[75] = 1
    else:
      features[75] = 0
    
    pass

  def check_box_77_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_77.checked == True):
      features[76] = 1
    else:
      features[76] = 0
    
    pass

  def check_box_78_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_78.checked == True):
      features[77] = 1
    else:
      features[77] = 0
    
    pass

  def check_box_79_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_79.checked == True):
      features[78] = 1
    else:
      features[78] = 0
    
    pass

  def check_box_80_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_80.checked == True):
      features[79] = 1
    else:
      features[79] = 0
    
    pass

  def check_box_81_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_81.checked == True):
      features[80] = 1
    else:
      features[80] = 0
    
    pass

  def check_box_82_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_82.checked == True):
      features[81] = 1
    else:
      features[81] = 0
    
    pass

  def check_box_83_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_83.checked == True):
      features[82] = 1
    else:
      features[82] = 0
    
    pass

  def check_box_84_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_84.checked == True):
      features[83] = 1
    else:
      features[83] = 0
    
    pass

  def check_box_85_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_85.checked == True):
      features[84] = 1
    else:
      features[84] = 0
    
    pass

  def check_box_86_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_86.checked == True):
      features[85] = 1
    else:
      features[85] = 0
    
    pass

  def check_box_87_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_87.checked == True):
      features[86] = 1
    else:
      features[86] = 0
    
    pass

  def check_box_88_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_88.checked == True):
      features[87] = 1
    else:
      features[87] = 0
    
    pass

  def check_box_89_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_89.checked == True):
      features[88] = 1
    else:
      features[88] = 0
    
    pass

  def check_box_90_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_90.checked == True):
      features[89] = 1
    else:
      features[89] = 0
    
    pass

  def check_box_91_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_91.checked == True):
      features[90] = 1
    else:
      features[90] = 0
    
    pass

  def check_box_92_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_92.checked == True):
      features[91] = 1
    else:
      features[91] = 0
    
    pass

  def check_box_93_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_93.checked == True):
      features[92] = 1
    else:
      features[92] = 0
    
    pass

  def check_box_94_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_94.checked == True):
      features[93] = 1
    else:
      features[93] = 0
    
    pass

  def check_box_95_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_95.checked == True):
      features[94] = 1
    else:
      features[94] = 0
    
    pass

  def check_box_96_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_96.checked == True):
      features[95] = 1
    else:
      features[95] = 0
    
    pass

  def check_box_97_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_97.checked == True):
      features[96] = 1
    else:
      features[96] = 0
    
    pass

  def check_box_98_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_98.checked == True):
      features[97] = 1
    else:
      features[97] = 0
    
    pass

  def check_box_99_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_99.checked == True):
      features[98] = 1
    else:
      features[98] = 0
    
    pass

  def check_box_100_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_100.checked == True):
      features[99] = 1
    else:
      features[99] = 0
    
    pass

  def check_box_101_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_101.checked == True):
      features[100] = 1
    else:
      features[100] = 0
    
    pass

  def check_box_102_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_102.checked == True):
      features[101] = 1
    else:
      features[101] = 0
    
    pass

  def check_box_103_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_103.checked == True):
      features[102] = 1
    else:
      features[102] = 0
    
    pass

  def check_box_104_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_104.checked == True):
      features[103] = 1
    else:
      features[103] = 0
    
    pass

  def check_box_105_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_105.checked == True):
      features[104] = 1
    else:
      features[104] = 0
    
    pass

  def check_box_106_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_106.checked == True):
      features[105] = 1
    else:
      features[105] = 0
    
    pass

  def check_box_107_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_107.checked == True):
      features[106] = 1
    else:
      features[106] = 0
    
    pass

  def check_box_108_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_108.checked == True):
      features[107] = 1
    else:
      features[107] = 0
    
    pass

  def check_box_109_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_109.checked == True):
      features[108] = 1
    else:
      features[108] = 0
    
    pass

  def check_box_110_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_110.checked == True):
      features[109] = 1
    else:
      features[109] = 0
    
    pass

  def check_box_111_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_111.checked == True):
      features[110] = 1
    else:
      features[110] = 0
    
    pass

  def check_box_112_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_112.checked == True):
      features[111] = 1
    else:
      features[111] = 0
    
    pass

  def check_box_113_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_113.checked == True):
      features[112] = 1
    else:
      features[112] = 0
    
    pass

  def check_box_114_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_114.checked == True):
      features[113] = 1
    else:
      features[113] = 0
    
    pass

  def check_box_115_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_115.checked == True):
      features[114] = 1
    else:
      features[114] = 0
    
    pass

  def check_box_116_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_116.checked == True):
      features[115] = 1
    else:
      features[115] = 0
    
    pass

  def check_box_117_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_117.checked == True):
      features[116] = 1
    else:
      features[116] = 0
    
    pass

  #features[117] is a duplicate symptom -- changes with checkbox 46
  
  def check_box_118_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_118.checked == True):
      features[118] = 1
    else:
      features[118] = 0
    
    pass

  def check_box_119_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_119.checked == True):
      features[119] = 1
    else:
      features[119] = 0
    
    pass

  def check_box_120_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_120.checked == True):
      features[120] = 1
    else:
      features[120] = 0
    
    pass

  def check_box_121_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_121.checked == True):
      features[121] = 1
    else:
      features[121] = 0
    
    pass

  def check_box_122_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_122.checked == True):
      features[122] = 1
    else:
      features[122] = 0
    
    pass

  def check_box_123_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_123.checked == True):
      features[123] = 1
    else:
      features[123] = 0
    
    pass

  def check_box_124_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_124.checked == True):
      features[124] = 1
    else:
      features[124] = 0
    
    pass

  def check_box_125_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_125.checked == True):
      features[125] = 1
    else:
      features[125] = 0
    
    pass

  def check_box_126_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_126.checked == True):
      features[126] = 1
    else:
      features[126] = 0
    
    pass

  def check_box_127_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_127.checked == True):
      features[127] = 1
    else:
      features[127] = 0
    
    pass

  def check_box_128_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_128.checked == True):
      features[128] = 1
    else:
      features[128] = 0
    
    pass

  def check_box_129_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_129.checked == True):
      features[129] = 1
    else:
      features[129] = 0
    
    pass

  def check_box_130_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_130.checked == True):
      features[130] = 1
    else:
      features[130] = 0
    
    pass

  def check_box_131_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.check_box_131.checked == True):
      features[131] = 1
    else:
      features[131] = 0
      
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.check_box_1.checked = False
    self.check_box_2.checked = False
    self.check_box_3.checked = False
    self.check_box_4.checked = False
    self.check_box_5.checked = False
    self.check_box_6.checked = False
    self.check_box_7.checked = False
    self.check_box_8.checked = False
    self.check_box_9.checked = False
    self.check_box_10.checked = False
    self.check_box_11.checked = False
    self.check_box_12.checked = False
    self.check_box_13.checked = False
    self.check_box_14.checked = False
    self.check_box_15.checked = False
    self.check_box_16.checked = False
    self.check_box_17.checked = False
    self.check_box_18.checked = False
    self.check_box_19.checked = False
    self.check_box_20.checked = False
    self.check_box_21.checked = False
    self.check_box_22.checked = False
    self.check_box_23.checked = False
    self.check_box_24.checked = False
    self.check_box_25.checked = False
    self.check_box_26.checked = False
    self.check_box_27.checked = False
    self.check_box_28.checked = False
    self.check_box_29.checked = False
    self.check_box_30.checked = False
    self.check_box_31.checked = False
    self.check_box_32.checked = False
    self.check_box_33.checked = False
    self.check_box_34.checked = False
    self.check_box_35.checked = False
    self.check_box_36.checked = False
    self.check_box_37.checked = False
    self.check_box_38.checked = False
    self.check_box_39.checked = False
    self.check_box_40.checked = False
    self.check_box_41.checked = False
    self.check_box_42.checked = False
    self.check_box_43.checked = False
    self.check_box_44.checked = False
    self.check_box_45.checked = False
    self.check_box_46.checked = False
    self.check_box_47.checked = False
    self.check_box_48.checked = False
    self.check_box_49.checked = False
    self.check_box_50.checked = False
    self.check_box_51.checked = False
    self.check_box_52.checked = False
    self.check_box_53.checked = False
    self.check_box_54.checked = False
    self.check_box_55.checked = False
    self.check_box_56.checked = False
    self.check_box_57.checked = False
    self.check_box_58.checked = False
    self.check_box_59.checked = False
    self.check_box_60.checked = False
    self.check_box_61.checked = False
    self.check_box_1.checked = False
    self.check_box_62.checked = False
    self.check_box_63.checked = False
    self.check_box_64.checked = False
    self.check_box_65.checked = False
    self.check_box_66.checked = False
    self.check_box_67.checked = False
    self.check_box_68.checked = False
    self.check_box_69.checked = False
    self.check_box_70.checked = False
    self.check_box_71.checked = False
    self.check_box_72.checked = False
    self.check_box_73.checked = False
    self.check_box_74.checked = False
    self.check_box_75.checked = False
    self.check_box_76.checked = False
    self.check_box_77.checked = False
    self.check_box_78.checked = False
    self.check_box_79.checked = False
    self.check_box_80.checked = False
    self.check_box_81.checked = False
    self.check_box_82.checked = False
    self.check_box_83.checked = False
    self.check_box_84.checked = False
    self.check_box_85.checked = False
    self.check_box_86.checked = False
    self.check_box_87.checked = False
    self.check_box_88.checked = False
    self.check_box_89.checked = False
    self.check_box_90.checked = False
    self.check_box_91.checked = False
    self.check_box_92.checked = False
    self.check_box_93.checked = False
    self.check_box_94.checked = False
    self.check_box_95.checked = False
    self.check_box_96.checked = False
    self.check_box_97.checked = False
    self.check_box_98.checked = False
    self.check_box_99.checked = False
    self.check_box_100.checked = False
    self.check_box_101.checked = False
    self.check_box_102.checked = False
    self.check_box_103.checked = False
    self.check_box_104.checked = False
    self.check_box_105.checked = False
    self.check_box_106.checked = False
    self.check_box_107.checked = False
    self.check_box_108.checked = False
    self.check_box_109.checked = False
    self.check_box_110.checked = False
    self.check_box_111.checked = False
    self.check_box_112.checked = False
    self.check_box_113.checked = False
    self.check_box_114.checked = False
    self.check_box_115.checked = False
    self.check_box_116.checked = False
    self.check_box_117.checked = False
    self.check_box_118.checked = False
    self.check_box_119.checked = False
    self.check_box_120.checked = False
    self.check_box_121.checked = False
    self.check_box_122.checked = False
    self.check_box_123.checked = False
    self.check_box_124.checked = False
    self.check_box_125.checked = False
    self.check_box_126.checked = False
    self.check_box_127.checked = False
    self.check_box_128.checked = False
    self.check_box_129.checked = False
    self.check_box_130.checked = False
    self.check_box_131.checked = False
    self.label_2.visible = False
    
    
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3')
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4')
    pass







 















