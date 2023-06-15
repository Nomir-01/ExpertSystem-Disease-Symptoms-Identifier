from pyknow import *

diseases_list = []
diseases_symptoms = []
diseases_symptoms_identification = []
d_sym_id = {}
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}


def preprocess():
    global diseases_list, diseases_symptoms, diseases_symptoms_identification, d_sym_id, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()

    for disease in diseases_list:
        disease_s_file = open("Disease symptoms identification/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_sym_id[disease] = disease_s_data
        disease_s_file.close()

        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()

        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()

        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


# def identify_disease(*arguments):
#	symptom_list = []
#	for symptom in arguments:
#		symptom_list.append(symptom)
#	return symptom_map[str(symptom_list)]

def get_symptom_identification(disease):
    return d_sym_id[disease]


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("-------------------------------------------------------")
    print("The best guessed disease is: %s" % id_disease)
    print("-------------------------------------------------------")
    print("Description of the disease:\n")
    print(disease_details)
    print("-------------------------------------------------------")
    print("Treatment of the disease:")
    print("-------------------------------------------------------")
    print(treatments)
    print("-------------------------------------------------------")


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("-------------------------------------------------------")
        print("This is an expert automated disease finder.\nPlease answer the following questions.")
        print("\nDo you feel any of the following symptoms: (yes/no)")
        print("")
        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), salience=1)
    def symptom_0(self):
        self.declare(Fact(headache=input("13.Headache: ")))

    @Rule(Fact(action='find_disease'), salience=2)
    def symptom_1(self):
        self.declare(Fact(back_pain=input("12.Back Pain: ")))

    @Rule(Fact(action='find_disease'), salience=3)
    def symptom_2(self):
        self.declare(Fact(chest_pain=input("11.Chest Pain: ")))

    @Rule(Fact(action='find_disease'), salience=4)
    def symptom_3(self):
        self.declare(Fact(cough=input("10.Cough: ")))

    @Rule(Fact(action='find_disease'), salience=5)
    def symptom_4(self):
        self.declare(Fact(fainting=input("9.Fainting: ")))

    @Rule(Fact(action='find_disease'), salience=6)
    def symptom_5(self):
        self.declare(Fact(fatigue=input("8.Fatigue: ")))

    @Rule(Fact(action='find_disease'), salience=7)
    def symptom_6(self):
        self.declare(Fact(sunken_eyes=input("7.Sunken Eyes: ")))

    @Rule(Fact(action='find_disease'), salience=8)
    def symptom_7(self):
        self.declare(Fact(low_body_temp=input("6.Low Body Temperature: ")))

    @Rule(Fact(action='find_disease'), salience=9)
    def symptom_8(self):
        self.declare(Fact(restlessness=input("5.Restlessness: ")))

    @Rule(Fact(action='find_disease'), salience=10)
    def symptom_9(self):
        self.declare(Fact(sore_throat=input("4.Sore Throat: ")))

    @Rule(Fact(action='find_disease'), salience=11)
    def symptom_10(self):
        self.declare(Fact(fever=input("3.Fever: ")))

    @Rule(Fact(action='find_disease'), salience=12)
    def symptom_11(self):
        self.declare(Fact(nausea=input("2.Nausea: ")))

    @Rule(Fact(action='find_disease'), salience=13)
    def symptom_12(self):
        self.declare(Fact(blurred_vision=input("1.Blurred Vision: ")))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_1(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="yes"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_2(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_4(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="yes"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_5(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_6(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_7(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="yes"))
    def disease_8(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="yes"))
    def disease_9(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_10(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_11(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="yes"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="yes"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_12(self):
        self.declare(Fact(disease="Hypothermia"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_13(self):
        self.declare(Fact(disease="None"))

    @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease), salience=-1)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("-------------------------------------------------------")
        print("The best guessed disease is: %s" % id_disease)
        print("-------------------------------------------------------")
        print("Description of the disease:\n")
        print(disease_details)
        print("-------------------------------------------------------")
        print("Treatment of the disease:\n")
        print(treatments)
        print("-------------------------------------------------------")

    @Rule(Fact(action='find_disease'),
          Fact(headache=MATCH.headache),
          Fact(back_pain=MATCH.back_pain),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fainting=MATCH.fainting),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(fatigue=MATCH.fatigue),
          Fact(low_body_temp=MATCH.low_body_temp),
          Fact(restlessness=MATCH.restlessness),
          Fact(fever=MATCH.fever),
          Fact(sunken_eyes=MATCH.sunken_eyes),
          Fact(nausea=MATCH.nausea),
          Fact(blurred_vision=MATCH.blurred_vision),
          NOT(Fact(disease=MATCH.disease)), salience=-2)
    def not_matched(self, headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,
                    low_body_temp, fever, sunken_eyes, nausea, blurred_vision):
        list = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness, low_body_temp,
                fever, sunken_eyes, nausea, blurred_vision]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(list)):
                if temp_list[j] == list[j] and list[j] == "yes":
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        not_matched(max_disease)


def disease_identification():
    preprocess()
    engine = Greetings()
    while 1:
        engine.reset()
        engine.run()
        print("-------------------------------------------------------")
        print("Would you like to diagnose some other symptoms? (y/n)")
        ch = input("Enter your choice: ")
        if ch == "no" or ch == "n":
            print("")
            main()


def symptom_identification():
    preprocess()
    print("Enter a disease name to know the symptoms of: ")
    for i in range(len(diseases_list)):
        print(diseases_list[i])
    dis_sym = input("\nEnter your choice: ")
    id_disease = dis_sym.title()
    print(id_disease)
    disease_symptoms_details = get_symptom_identification(id_disease)
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("-------------------------------------------------------")
    print("The Disease is: %s" % id_disease)
    print("-------------------------------------------------------")
    print("The Disease Symptom(s) Are: ")
    print(disease_symptoms_details)
    print("-------------------------------------------------------")
    print("Description of the disease:\n")
    print(disease_details)
    print("-------------------------------------------------------")
    print("Treatment of the disease:\n")
    print(treatments)
    print("-------------------------------------------------------")
    print("Would you like to diagnose some other disease? (y/n)")
    ch = input("Enter your choice: ")
    if ch == "no" or ch == "n":
        print("")
        main()
    else:
        symptom_identification()


def main():
    print("\n-------------------------")
    print("Medical Expert System")
    print("-------------------------\n")
    print("Select Your Choice:\n1.Disease Identification\n2.Symptom Identification")
    choice = input("\nEnter Your Choice: ")
    if choice == '1':
        disease_identification()
    elif choice == '2':
        symptom_identification()
    else:
        exit()


if __name__ == '__main__':
    main()