from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4')
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""

    #Dictionary containing emergency instructions
    emergency_instructions = {
    "choking": "\n1. Encourage the patient to cough.\n2. Bend them forwards and give them up to 5 back blows.\n3. If they are still choking, give them up to five abdominal thrusts.\n4. If they don't stop choking, call 911 (or your local emergency hotline) immediately.\n\n*Recommended by Red Cross UK*",
    "seizure": "\n1. Ease the person to the floor and turn them gently onto one side.\n2. Put something soft and flat under their head, and remove anything that can make it hard for them to breathe.\n3. Time the seizure.\n4. If the seizure lasts longer than 5 minutes, call 911 (or your local emergency hotline).                                           *Recommended by the CDC*",
    "passed out": "\n1. Prop up the person's legs about 12 inches (30 centimeters).\n2. Loosen belts, collars or other tight clothing.\n3. To reduce the chance of fainting again, don't get the person up too fast.\n4. If the person doesn't regain consciousness within one minute, call 911 (or your local emergency hotline).                                 *Recommended by the Mayo Clinic*",
    "heart attack": "\n1. Call 911 (or your local emergency hotline). A heart attack is a serious medical emergency that requires immediate care.\n2. Give the patient chest pain medicine, such as nitroglycerin. If chest pain medicine is not readily available, give them Aspirin.\n3. Stay Calm. While you are waiting for help, do not provide the patient with any other medication, unless recommended by a healthcare specialist.\n4. Begin CPR if the patient goes unconscious. This involves performing chest thrusts at an even rate of about 100-120 compressions per minute. Ensure that chest thrusts are firm and relatively quick. Try singing a song in your head to keep thrusts at an even rhythm.\n\n*Recommended by Cleveland Clinic*",
    "dehydration": "\nThe best way to treat this condition is to go to the hospital, as this is a serious emergency and may require IV (intravenous) fluids. Call 911 (or your local emergency hotline) immediately.                     *Recommended by Cedars Sinai*",
    "severe bleeding": "\n1. Wear protective covering and attempt to close the wound with a sterile bandaging or a non-fluffy cloth.\n2. Apply direct pressure on the bandaging, attempting to stop the blood flow.\n3. Best option, call 911 (or your local emergency hotline) immediately.               *Recommended by St. John's Ambulance UK*",
    "bleeding": "\n1. Wear protective covering and attempt to close the wound with a sterile bandaging or a non-fluffy cloth.\n2. Apply direct pressure on the bandaging, attempting to stop the blood flow.\n3. Best option, call 911 (or your local emergency hotline) immediately.                               *Recommended by St. John's Ambulance UK*",
    "gunshot wounds": "\n1. Call 911 (or your local emergency hotline) immediately.This is an extremely serious medical emergency.\n2. While waiting for the paramedics, try to stop the bleeding using direct pressure with a sterile cloth.\n3. Don't elevate the body part.                        *Recommended by Verywell Health*",
    "gunshot": "\n1. Call 911 (or your local emergency hotline) immediately.This is an extremely serious medical emergency.\n2. While waiting for the paramedics, try to stop the bleeding using direct pressure with a sterile cloth.\n3. Don't elevate the body part.                                      *Recommended by Verywell Health*",
    "stab wounds": "\n1. Survey the area.\n2. Call 911 (or your local emergency hotline) immediately.\n3. Check for injuries, and the ABCs (Airways, Breathing, Circulation).\n4. Do NOT remove the stabbing object and cover the dressing.\n5. Continue to apply pressure until help arrives.               *Recommended by First Aid Courses -- Darwin, AUS*",
    "stabbing": "\n1. Survey the area.\n2. Call 911 (or your local emergency hotline) immediately.\n3. Check for injuries, and the ABCs (Airways, Breathing, Circulation).\n4. Do NOT remove the stabbing object and cover the dressing.\n5. Continue to apply pressure until help arrives.               *Recommended by First Aid Courses -- Darwin, AUS*",
    "poisoning": "\n1. If the person is not breathing, call 911. If the person inhaled poison, get him or her fresh air right away.\n2.If the person has poison on the skin, take off any clothing the poison touched.\n3.Rinse skin with running water for 15 to 20 minutes.\n4.If the person has poison in the eyes, rinse eyes with running water for 15 to 20 minutes. *Recommended by Health Resources and Services Administration*",
    "stroke": "\n1. Wear protective covering and attempt to close the wound with a sterile bandaging or a non-fluffy cloth.\n2. Apply direct pressure on the bandaging, attempting to stop the blood flow.\n3. Best option, call 911 (or your local emergency hotline) immediately.               *Recommended by St. John's Ambulance UK*",
    "burns": "\n1. Avoid handling the affected area more than necessary. See that your hands are as clean as possible by washing them.\n2. Do not apply lotions of any kind.\n3. Do not remove burned clothing and do not break blisters.\n4. Cover the area (including burned clothing), with a dry sterile dressing if possible, or similar material such as clean lint, freshly-laundered linen.\n5. Bandage firmly, except when blisters are present or suspected, in which case, bandage lightly.\n6. Immobilise the area by suitable means. *From The Better India*",
    "scalds": "\n1. Avoid handling the affected area more than necessary. See that your hands are as clean as possible by washing them.\n2. Do not apply lotions of any kind.\n3. Do not remove burned clothing and do not break blisters.\n4. Cover the area (including burned clothing), with a dry sterile dressing if possible, or similar material such as clean lint, freshly-laundered linen.\n5. Bandage firmly, except when blisters are present or suspected, in which case, bandage lightly.\n6. Immobilise the area by suitable means. *From The Better India*",
    "heat stroke": "\n1. Placing the person in a tub of cool water or a cool shower\n2. Spray with a garden hose\n3. Sponge with cold water\n4. Fan while misting with cool water\n5. Place ice packs or cool, wet towels on the neck, armpits and groin\n6. Cover with cool, damp sheets *From The Better India*",
    "fracture": "\n1. Treat the fracture on the spot.\n2. Steady and support the injured parts at once, so that movement is impossible.\n3. Immobilise the fracture by the use of bandages or the use of splints. Never apply a bandage over the site of a fracture. They must be applied sufficiently firmly to prevent harmful movements, but not so tightly as to prevent the circulation of blood. *From The Better India*",
    "broken bone": "\n1. Treat the fracture on the spot.\n2. Steady and support the injured parts at once, so that movement is impossible.\n3. Immobilise the fracture by the use of bandages or the use of splints. Never apply a bandage over the site of a fracture. They must be applied sufficiently firmly to prevent harmful movements, but not so tightly as to prevent the circulation of blood. *From The Better India*",
    "electrocution": "\n1. Switch off the current, and if it cannot be put off, cut off supply by removing the plug, breaking the cable or wrenching it free.\n2. Remove the patient from contact with the current with the greatest care, using dry insulating materials.\n3. Lay the patient down on their back, with the head low and turned to one side unless there is an injury to the head, abdomen or chest when the head and shoulders should be slightly raised and supported.\n4. Loosen clothing around the neck, chest and waist./n5. Wrap them in a blanket or rug.\n6. Give sips of water, coffee or any liquid but never alcohol. *From The Better India*",
    "sting": "\n1. If it is a bee, wasp or hornet sting, remove the sting with a pair of tweezers. If tweezers aren’t available, apply pressure around the sting to force it out.\n2. Wash thoroughly with soap and water, and apply an antihistamine ointment or lotion to relieve itching.\n3. Avoid scratching the bites. *From The Better India*",
    "animal bites": "\nDog and cat bites are usually small, punctured wounds and should be treated by covering with a clean, dry dressing. If the animal is rabid, please get medical emergency help immediately.\n1. Wash the wound with water to remove bacteria-filled saliva of the animal.\n2. Keep the bitten part low.\n3. Bathe the wound with a weak solution of permanganate of potash, if available.\n4. Apply a clean dressing after taking care that the wound has been cauterised. *From The Better India*",
    "animal scratches": "\n1. If the bite or scratch is shallow and from an immunized household pet in good health, wash the wound for at least 5 minutes with soap and water. Avoid scrubbing the injury, which could lead to bruising. Use an antiseptic ointment or cream. Once the injury has been treated, watch for infections. Symptoms include swelling, redness, pain, fever, or drainage. If you notice any of these symptoms, call a healthcare provider./n2. If the injury is from an animal unknown to you or the wound is deep, follow these steps: Apply pressure to the injury if it is bleeding with a clean towel or bandage to help stop bleeding. Use soap and water to wash the wound for at least five minutes. Avoid scrubbing because it may lead to bruising. Dry the wound and wrap it with a sterile dressing. Avoid butterfly bandages or tape as these could potentially trap bacteria in the wound. *From Patient Urgent Care Clinic*",
    "eye injury": "\n1. Prevent the patient from rubbing the eye, and set them facing the light, standing in front of them.\n2. Pull down the lower eyelid, and if the foreign body is seen and isn’t embedded, remove it with the corner of a clean handkerchief, preferably white, twirled up and moistened with water.\n3. If the body is embedded, do not attempt to remove it, but instruct the patient to close their eyes. Apply a soft pad of cotton wool and secure it with a bandage.\n4. If the foreign body is not found and is suspected to be under the upper eyelid, instruct the patient to blink under water. Alternatively, lift the upper lid forward, push the lower lid beneath it and let go of both eyelids. The lashes of the lower lid may brush the inner surface of the upper one, and dislodge the foreign body. *From The Better India*",
    
   # Add more emergencies and corresponding instructions here
    }
    
    search_query = self.text_box_1.text.lower()
    if search_query in emergency_instructions:
        instructions = emergency_instructions[search_query]
    elif (search_query == ""):
      instructions = "\nPlease describe your emergency situation using the text box above."
    else:
        instructions = "\nWe do not have this situation on file. Please call 9-1-1 for emergency assistance."
    self.label_1.text = instructions
    self.label_1.visible = True
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

    #Dictionary containing emergency instructions
    emergency_instructions = {
    "choking": "\n1. Encourage the patient to cough.\n2. Bend them forwards and give them up to 5 back blows.\n3. If they are still choking, give them up to five abdominal thrusts.\n4. If they don't stop choking, call 911 (or your local emergency hotline) immediately.\n\n*Recommended by Red Cross UK*",
    "seizure": "\n1. Ease the person to the floor and turn them gently onto one side.\n2. Put something soft and flat under their head, and remove anything that can make it hard for them to breathe.\n3. Time the seizure.\n4. If the seizure lasts longer than 5 minutes, call 911 (or your local emergency hotline).                                           *Recommended by the CDC*",
    "passed out": "\n1. Prop up the person's legs about 12 inches (30 centimeters).\n2. Loosen belts, collars or other tight clothing.\n3. To reduce the chance of fainting again, don't get the person up too fast.\n4. If the person doesn't regain consciousness within one minute, call 911 (or your local emergency hotline).                                 *Recommended by the Mayo Clinic*",
    "heart attack": "\n1. Call 911 (or your local emergency hotline). A heart attack is a serious medical emergency that requires immediate care.\n2. Give the patient chest pain medicine, such as nitroglycerin. If chest pain medicine is not readily available, give them Aspirin.\n3. Stay Calm. While you are waiting for help, do not provide the patient with any other medication, unless recommended by a healthcare specialist.\n4. Begin CPR if the patient goes unconscious. This involves performing chest thrusts at an even rate of about 100-120 compressions per minute. Ensure that chest thrusts are firm and relatively quick. Try singing a song in your head to keep thrusts at an even rhythm.\n\n*Recommended by Cleveland Clinic*",
    "dehydration": "\nThe best way to treat this condition is to go to the hospital, as this is a serious emergency and may require IV (intravenous) fluids. Call 911 (or your local emergency hotline) immediately.                     *Recommended by Cedars Sinai*",
    "severe bleeding": "\n1. Wear protective covering and attempt to close the wound with a sterile bandaging or a non-fluffy cloth.\n2. Apply direct pressure on the bandaging, attempting to stop the blood flow.\n3. Best option, call 911 (or your local emergency hotline) immediately.               *Recommended by St. John's Ambulance UK*",
    "bleeding": "\n1. Wear protective covering and attempt to close the wound with a sterile bandaging or a non-fluffy cloth.\n2. Apply direct pressure on the bandaging, attempting to stop the blood flow.\n3. Best option, call 911 (or your local emergency hotline) immediately.                               *Recommended by St. John's Ambulance UK*",
    "gunshot wounds": "\n1. Call 911 (or your local emergency hotline) immediately.This is an extremely serious medical emergency.\n2. While waiting for the paramedics, try to stop the bleeding using direct pressure with a sterile cloth.\n3. Don't elevate the body part.                        *Recommended by Verywell Health*",
    "gunshot": "\n1. Call 911 (or your local emergency hotline) immediately.This is an extremely serious medical emergency.\n2. While waiting for the paramedics, try to stop the bleeding using direct pressure with a sterile cloth.\n3. Don't elevate the body part.                                      *Recommended by Verywell Health*",
    "stab wounds": "\n1. Survey the area.\n2. Call 911 (or your local emergency hotline) immediately.\n3. Check for injuries, and the ABCs (Airways, Breathing, Circulation).\n4. Do NOT remove the stabbing object and cover the dressing.\n5. Continue to apply pressure until help arrives.               *Recommended by First Aid Courses -- Darwin, AUS*",
    "stabbing": "\n1. Survey the area.\n2. Call 911 (or your local emergency hotline) immediately.\n3. Check for injuries, and the ABCs (Airways, Breathing, Circulation).\n4. Do NOT remove the stabbing object and cover the dressing.\n5. Continue to apply pressure until help arrives.               *Recommended by First Aid Courses -- Darwin, AUS*",
    "poisoning": "\n1. If the person is not breathing, call 911. If the person inhaled poison, get him or her fresh air right away.\n2.If the person has poison on the skin, take off any clothing the poison touched.\n3.Rinse skin with running water for 15 to 20 minutes.\n4.If the person has poison in the eyes, rinse eyes with running water for 15 to 20 minutes. *Recommended by Health Resources and Services Administration*",
    "stroke": "\n1. Wear protective covering and attempt to close the wound with a sterile bandaging or a non-fluffy cloth.\n2. Apply direct pressure on the bandaging, attempting to stop the blood flow.\n3. Best option, call 911 (or your local emergency hotline) immediately.               *Recommended by St. John's Ambulance UK*",
    "burns": "\n1. Avoid handling the affected area more than necessary. See that your hands are as clean as possible by washing them.\n2. Do not apply lotions of any kind.\n3. Do not remove burned clothing and do not break blisters.\n4. Cover the area (including burned clothing), with a dry sterile dressing if possible, or similar material such as clean lint, freshly-laundered linen.\n5. Bandage firmly, except when blisters are present or suspected, in which case, bandage lightly.\n6. Immobilise the area by suitable means. *From The Better India*",
    "scalds": "\n1. Avoid handling the affected area more than necessary. See that your hands are as clean as possible by washing them.\n2. Do not apply lotions of any kind.\n3. Do not remove burned clothing and do not break blisters.\n4. Cover the area (including burned clothing), with a dry sterile dressing if possible, or similar material such as clean lint, freshly-laundered linen.\n5. Bandage firmly, except when blisters are present or suspected, in which case, bandage lightly.\n6. Immobilise the area by suitable means. *From The Better India*",
    "heat stroke": "\n1. Placing the person in a tub of cool water or a cool shower\n2. Spray with a garden hose\n3. Sponge with cold water\n4. Fan while misting with cool water\n5. Place ice packs or cool, wet towels on the neck, armpits and groin\n6. Cover with cool, damp sheets *From The Better India*",
    "fracture": "\n1. Treat the fracture on the spot.\n2. Steady and support the injured parts at once, so that movement is impossible.\n3. Immobilise the fracture by the use of bandages or the use of splints. Never apply a bandage over the site of a fracture. They must be applied sufficiently firmly to prevent harmful movements, but not so tightly as to prevent the circulation of blood. *From The Better India*",
    "broken bone": "\n1. Treat the fracture on the spot.\n2. Steady and support the injured parts at once, so that movement is impossible.\n3. Immobilise the fracture by the use of bandages or the use of splints. Never apply a bandage over the site of a fracture. They must be applied sufficiently firmly to prevent harmful movements, but not so tightly as to prevent the circulation of blood. *From The Better India*",
    "electrocution": "\n1. Switch off the current, and if it cannot be put off, cut off supply by removing the plug, breaking the cable or wrenching it free.\n2. Remove the patient from contact with the current with the greatest care, using dry insulating materials.\n3. Lay the patient down on their back, with the head low and turned to one side unless there is an injury to the head, abdomen or chest when the head and shoulders should be slightly raised and supported.\n4. Loosen clothing around the neck, chest and waist./n5. Wrap them in a blanket or rug.\n6. Give sips of water, coffee or any liquid but never alcohol. *From The Better India*",
    "sting": "\n1. If it is a bee, wasp or hornet sting, remove the sting with a pair of tweezers. If tweezers aren’t available, apply pressure around the sting to force it out.\n2. Wash thoroughly with soap and water, and apply an antihistamine ointment or lotion to relieve itching.\n3. Avoid scratching the bites. *From The Better India*",
    "animal bites": "\nDog and cat bites are usually small, punctured wounds and should be treated by covering with a clean, dry dressing. If the animal is rabid, please get medical emergency help immediately.\n1. Wash the wound with water to remove bacteria-filled saliva of the animal.\n2. Keep the bitten part low.\n3. Bathe the wound with a weak solution of permanganate of potash, if available.\n4. Apply a clean dressing after taking care that the wound has been cauterised. *From The Better India*",
    "animal scratches": "\n1. If the bite or scratch is shallow and from an immunized household pet in good health, wash the wound for at least 5 minutes with soap and water. Avoid scrubbing the injury, which could lead to bruising. Use an antiseptic ointment or cream. Once the injury has been treated, watch for infections. Symptoms include swelling, redness, pain, fever, or drainage. If you notice any of these symptoms, call a healthcare provider./n2. If the injury is from an animal unknown to you or the wound is deep, follow these steps: Apply pressure to the injury if it is bleeding with a clean towel or bandage to help stop bleeding. Use soap and water to wash the wound for at least five minutes. Avoid scrubbing because it may lead to bruising. Dry the wound and wrap it with a sterile dressing. Avoid butterfly bandages or tape as these could potentially trap bacteria in the wound. *From Patient Urgent Care Clinic*",
    "eye injury": "\n1. Prevent the patient from rubbing the eye, and set them facing the light, standing in front of them.\n2. Pull down the lower eyelid, and if the foreign body is seen and isn’t embedded, remove it with the corner of a clean handkerchief, preferably white, twirled up and moistened with water.\n3. If the body is embedded, do not attempt to remove it, but instruct the patient to close their eyes. Apply a soft pad of cotton wool and secure it with a bandage.\n4. If the foreign body is not found and is suspected to be under the upper eyelid, instruct the patient to blink under water. Alternatively, lift the upper lid forward, push the lower lid beneath it and let go of both eyelids. The lashes of the lower lid may brush the inner surface of the upper one, and dislodge the foreign body. *From The Better India*",
    
   # Add more emergencies and corresponding instructions here
    }
    
    search_query = self.text_box_1.text.lower()
    if search_query in emergency_instructions:
        instructions = emergency_instructions[search_query]
    elif (search_query == ""):
      instructions = "\nPlease describe your emergency situation using the text box above."
    else:
        instructions = "\nWe do not have this situation on file. Please call 9-1-1 for emergency assistance."
    self.label_1.text = instructions
    self.label_1.visible = True
    pass








