"""MeSH qualifiers from raw/mesh/q2020.bin."""

# 76 items in total:
# 76 SH Name
# 76 QA Abbreviation
# 76 QE Short Form
# 76 MS Scope Note

from collections import namedtuple

NtQbin = namedtuple('NtQbin', 'SH QA QE MS')
NTS = [
  NtQbin._make(['abnormalities', 'AB', 'ABNORM', 'Used with organs for congenital defects producing changes in the morphology of the organ. It is used also for abnormalities in animals.']),
  NtQbin._make(['administration & dosage', 'AD', 'ADMIN', 'Used with drugs for dosage forms, routes of administration, frequency and duration of administration, quantity of medication, and the effects of these factors.']),
  NtQbin._make(['adverse effects', 'AE', 'ADV EFF', 'Used with drugs, chemicals, or biological agents in accepted dosage - or with physical agents or manufactured products in normal usage - when intended for diagnostic, therapeutic, prophylactic, or anesthetic purposes. It is used also for adverse effects or complications of diagnostic, therapeutic, prophylactic, anesthetic, surgical, or other procedures.']),
  NtQbin._make(['agonists', 'AG', 'AGON', 'Used with chemicals, drugs, and endogenous substances to indicate substances or agents that have affinity for a receptor and intrinsic activity at that receptor. (From Textbook of Pharmacology, 1991, p.16)']),
  NtQbin._make(['analogs & derivatives', 'AA', 'ANALOGS', 'Used with drugs and chemicals for substances that share the same parent molecule or have similar electronic structure but differ by the addition or substitution of other atoms or molecules. It is used when the specific chemical heading is not available and no appropriate group heading exists.']),
  NtQbin._make(['analysis', 'AN', 'ANAL', 'Used for the identification or quantitative determination of a substance or its constituents and metabolites; includes the analysis of air, water, or other environmental carrier. It excludes the chemical analysis of tissues, tumors, body fluids, organisms, and plants for which "chemistry" is used. The concept applies to both methodology and results. For analysis of substances in blood, cerebrospinal fluid, and urine the specific subheading designating the fluid is used.']),
  NtQbin._make(['anatomy & histology', 'AH', 'ANAT', 'Used with organs, regions, and tissues for normal descriptive anatomy and histology, and for the normal anatomy and structure of animals and plants.']),
  NtQbin._make(['antagonists & inhibitors', 'AI', 'ANTAG', 'Used with chemicals, drugs, and endogenous substances to indicate substances or agents which counteract their biological effects by any mechanism.']),
  NtQbin._make(['biosynthesis', 'BI', 'BIOSYN', 'Used for the anabolic formation of chemical substances in organisms, in living cells, or by subcellular fractions.']),
  NtQbin._make(['blood', 'BL', 'BLOOD', 'Used for the presence or analysis of substances in the blood; also for examination of, or changes in, the blood in disease states. It excludes serodiagnosis, for which the subheading "diagnosis" is used, and serology, for which "immunology" is used.']),
  NtQbin._make(['blood supply', 'BS', 'BLOOD SUPPLY', 'Used for arterial, capillary, and venous systems of an organ or region whenever the specific heading for the vessel does not exist. It includes blood flow through the organ.']),
  NtQbin._make(['cerebrospinal fluid', 'CF', 'CSF', 'Used for the presence or analysis of substances in the cerebrospinal fluid; also for examination of or changes in cerebrospinal fluid in disease states.']),
  NtQbin._make(['chemical synthesis', 'CS', 'CHEM SYN', 'Used for the chemical preparation of molecules in vitro. For the formation of chemical substances in organisms, living cells, or subcellular fractions, "biosynthesis" is used.']),
  NtQbin._make(['chemically induced', 'CI', 'CHEM IND', 'Used for biological phenomena, diseases, syndromes, congenital abnormalities, or symptoms caused by endogenous or exogenous substances.']),
  NtQbin._make(['chemistry', 'CH', 'CHEM', 'Used with chemicals, biological, and non-biological substances for their composition, structure, characterization, and properties; also used for the chemical composition or content of organs, tissue, tumors, body fluids, organisms, and plants. Excludes chemical analysis and determination of substances for which "analysis" is used; excludes synthesis for which "chemical synthesis" is used; excludes isolation and purification of substances for which "isolation & purification" is used.']),
  NtQbin._make(['classification', 'CL', 'CLASS', 'Used for taxonomic or other systematic or hierarchical classification systems.']),
  NtQbin._make(['complications', 'CO', 'COMPL', 'Used with diseases to indicate conditions that co-exist or follow, i.e., co-existing diseases, complications, or sequelae.']),
  NtQbin._make(['congenital', 'CN', 'CONGEN', 'Used with disease headings to indicate those conditions existing at, and usually before, birth. It excludes morphologic abnormalities and birth injuries, for which "abnormalities" and "injuries" are used.']),
  NtQbin._make(['cytology', 'CY', 'CYTOL', 'Used for cellular appearance of unicellular and multicellular organisms.']),
  NtQbin._make(['deficiency', 'DF', 'DEFIC', 'Used with endogenous and exogenous substances which are absent or in diminished amount relative to the normal requirement of an organism or a biologic system.']),
  NtQbin._make(['diagnosis', 'DI', 'DIAG', 'Used with diseases for all aspects of diagnosis, including examination, differential diagnosis and prognosis. Excludes diagnosis using imaging techniques (e.g. radiography, scintigraphy, and ultrasonography) for which "diagnostic imaging" is used.']),
  NtQbin._make(['diagnostic imaging', 'DG', 'DIAG IMAGE', 'Used for the visualization of an anatomical structure or for the diagnosis of disease.  Commonly used imaging techniques include radiography, radionuclide imaging, thermography, tomography, and ultrasonography']),
  NtQbin._make(['diet therapy', 'DH', 'DIET THER', 'Used with disease headings for dietary and nutritional management of the disease. The concept does not include vitamin or mineral supplements, for which "drug therapy" may be used.']),
  NtQbin._make(['drug effects', 'DE', 'DRUG EFF', 'Used with organs, regions, tissues, or organisms and physiological and psychological processes for the effects of drugs and chemicals.']),
  NtQbin._make(['drug therapy', 'DT', 'DRUG THER', 'Used with disease headings for the treatment of disease by the administration of drugs, chemicals, and antibiotics. For diet therapy and radiotherapy, use  specific subheadings. Excludes immunotherapy for which "therapy" is used.']),
  NtQbin._make(['economics', 'EC', 'ECON', 'Used for the economic aspects of any subject, as well as for all aspects of financial management. It includes the raising or providing of funds.']),
  NtQbin._make(['education', 'ED', 'EDUC', 'Used for education, training programs, and courses in various fields and disciplines, and for training groups of persons.']),
  NtQbin._make(['embryology', 'EM', 'EMBRYOL', 'Used with organs, regions, and animal headings for embryologic and fetal development. It is used also with diseases for embryologic factors contributing to postnatal disorders.']),
  NtQbin._make(['enzymology', 'EN', 'ENZYMOL', 'Used with organisms, except vertebrates, and with organs and tissues. It is also used with diseases for enzymes during the course of the disease, but excludes diagnostic enzyme tests, for which "diagnosis" is used.']),
  NtQbin._make(['epidemiology', 'EP', 'EPIDEMIOL', 'Used with human and veterinary diseases for the distribution of disease, factors which cause disease, and the attributes of disease in defined populations; includes incidence, frequency, prevalence, endemic and epidemic outbreaks; also surveys and estimates of morbidity in geographic areas and in specified populations. Used also with geographical headings for the location of epidemiologic aspects of a disease. Excludes mortality for which "mortality" is used.']),
  NtQbin._make(['ethics', 'ES', 'ETHICS', 'Used with techniques and activities for discussion and analysis with respect to human and social values.']),
  NtQbin._make(['ethnology', 'EH', 'ETHNOL', 'Used with diseases for ethnic, cultural, or anthropological aspects, and with geographic headings to indicate the place of origin of a group of people.']),
  NtQbin._make(['etiology', 'ET', 'ETIOL', 'Used with diseases for causative agents including microorganisms and includes environmental and social factors and personal habits as contributing factors. It includes pathogenesis.']),
  NtQbin._make(['genetics', 'GE', 'GENET', 'Used for mechanisms of heredity and the genetics of organisms, for the genetic basis of normal and pathologic states, and for the genetic aspects of endogenous chemicals. It includes biochemical and molecular influence on genetic material.']),
  NtQbin._make(['growth & development', 'GD', 'GROWTH', 'Used with microorganisms, plants, and the postnatal period of animals for growth and development. It includes also the postnatal growth or development of organs or anatomical parts. For prenatal period of animals for growth and development use /embryology.']),
  NtQbin._make(['history', 'HI', 'HIST', 'Used for the historical aspects of any subject. It includes brief historical notes but excludes case histories.']),
  NtQbin._make(['immunology', 'IM', 'IMMUNOL', 'Used for immunologic studies of tissues, organs, microorganisms, fungi, viruses, and animals. It includes immunologic aspects of diseases but not immunologic procedures used for diagnostic, preventive, or therapeutic purposes, for which "diagnosis", "prevention & control", or "therapy" are used. The concept is also used for chemicals as antigens or haptens.']),
  NtQbin._make(['injuries', 'IN', 'INJ', 'Used with anatomic headings, animals, and sports for wounds and injuries. Excludes cell damage, for which "pathology" is used.']),
  NtQbin._make(['innervation', 'IR', 'INNERV', 'Used with organs, regions, or tissues for their nerve supply.']),
  NtQbin._make(['instrumentation', 'IS', 'INSTRUM', 'Used with diagnostic or therapeutic procedures, analytic techniques, and specialties or disciplines, for the development or modification of apparatus, instruments, or equipment.']),
  NtQbin._make(['isolation & purification', 'IP', 'ISOL', 'Used with bacteria, viruses, fungi, protozoa, and helminths for the obtaining of pure strains or for the demonstration of the presence of or identification of organisms by DNA analyses, immunologic, or other methods, including culture techniques. It is used also with biological substances and chemicals for the isolation and purification of the constituents.']),
  NtQbin._make(['legislation & jurisprudence', 'LJ', 'LEGIS', 'Used for laws, statutes, ordinances, or government regulations, as well as for legal controversy and court decisions.']),
  NtQbin._make(['metabolism', 'ME', 'METAB', 'Used with organs, cells and subcellular fractions, organisms, and diseases for biochemical changes. It is used also with drugs and chemicals for catabolic changes (breakdown of complex molecules into simpler ones). For anabolic processes (conversion of small molecules into large), BIOSYNTHESIS is used. For enzymology and pharmacokinetics use the specific subheadings.']),
  NtQbin._make(['methods', 'MT', 'METHODS', 'Used with techniques, procedures, and programs for methods.']),
  NtQbin._make(['microbiology', 'MI', 'MICROBIOL', 'Used with organs, animals, and higher plants and with diseases for microbiologic studies. For parasites, "parasitology" is used; for viruses, "virology" is used.']),
  NtQbin._make(['mortality', 'MO', 'MORTAL', 'Used with human and veterinary diseases for mortality statistics. For deaths resulting from various procedures statistically but for a death resulting in a specific case, use FATAL OUTCOME, not /mortality.']),
  NtQbin._make(['nursing', 'NU', 'NURS', 'Used with diseases for nursing care and techniques in their management. It includes the nursing role in diagnostic, therapeutic, and preventive procedures.']),
  NtQbin._make(['organization & administration', 'OG', 'ORGAN', 'Used for administrative structure and management.']),
  NtQbin._make(['parasitology', 'PS', 'PARASITOL', 'Used with animals, higher plants, organs, and diseases for parasitic factors. In diseases, it is not used if the parasitic involvement is implicit in the diagnosis.']),
  NtQbin._make(['pathogenicity', 'PY', 'PATHOGEN', 'Used with microorganisms, viruses, and parasites for studies of their ability to cause disease in man, animals, or plants.']),
  NtQbin._make(['pathology', 'PA', 'PATHOL', 'Used for organ, tissue, or cell structure in disease states.']),
  NtQbin._make(['pharmacokinetics', 'PK', 'PHARMACOKIN', 'Used for the mechanism, dynamics and kinetics of exogenous chemical and drug absorption, biotransformation, distribution, release, transport, uptake and elimination as a function of dosage, extent and rate of metabolic processes.']),
  NtQbin._make(['pharmacology', 'PD', 'PHARMACOL', 'Used with drugs and exogenously administered chemical substances for their effects on living tissues and organisms. It includes acceleration and inhibition of physiological and biochemical processes and other pharmacologic mechanisms of action.']),
  NtQbin._make(['physiology', 'PH', 'PHYSIOL', 'Used with organs, tissues, and cells of unicellular and multicellular organisms for normal function. It is used also with biochemical substances, endogenously produced, for their physiologic role.']),
  NtQbin._make(['physiopathology', 'PP', 'PHYSIOPATHOL', 'Used with organs and diseases for disordered function in disease states.']),
  NtQbin._make(['poisoning', 'PO', 'POIS', 'Used with drugs, chemicals, and industrial materials for human or animal poisoning, acute or chronic, whether the poisoning is accidental, occupational, suicidal, by medication error, or by environmental exposure.']),
  NtQbin._make(['prevention & control', 'PC', 'PREV', 'Used with disease headings for increasing human or animal resistance against disease (e.g., immunization), for control of transmission agents, for prevention and control of environmental hazards, or for prevention and control of social factors leading to disease. It includes preventive measures in individual cases.']),
  NtQbin._make(['psychology', 'PX', 'PSYCHOL', 'Used with non-psychiatric diseases, techniques, and named groups for psychologic, psychiatric, psychosomatic, psychosocial, behavioral, and emotional aspects, and with psychiatric disease for psychologic aspects; used also with animal terms for animal behavior and psychology.']),
  NtQbin._make(['radiation effects', 'RE', 'RAD EFF', 'Used for effects of ionizing and nonionizing radiation upon living organisms, organs and tissues, and their constituents, and upon physiologic processes. It includes the effect of irradiation on drugs and chemicals.']),
  NtQbin._make(['radiotherapy', 'RT', 'RADIOTHER', 'Used with disease headings for the therapeutic use of ionizing and nonionizing radiation. It includes the use of radioisotope therapy.']),
  NtQbin._make(['rehabilitation', 'RH', 'REHABIL', 'Used with diseases and surgical procedures for restoration of function of the individual.']),
  NtQbin._make(['secondary', 'SC', 'SECOND', 'Used with neoplasms to indicate the secondary location to which the neoplastic process has metastasized.']),
  NtQbin._make(['standards', 'ST', 'STAND', 'Used with facilities, personnel, and program headings for the development, testing, and application of standards of adequacy or acceptable performance and with chemicals and drugs for standards of identification, quality, and potency. It includes health or safety standards in industries and occupations.']),
  NtQbin._make(['statistics & numerical data', 'SN', 'STATIST', 'Used with non-disease headings for the expression of numerical values that describe particular sets or groups of data. It includes level of use of equipment and supplies, facilities and services and procedures and techniques. It excludes supply or demand for which "supply & distribution" is used']),
  NtQbin._make(['supply & distribution', 'SD', 'SUPPLY', 'Used for the quantitative availability and distribution of material, equipment, health services, personnel, and facilities. It excludes food supply and water supply in industries and occupations.']),
  NtQbin._make(['surgery', 'SU', 'SURG', 'Used for operative procedures on organs, regions, or tissues in the treatment of diseases, including tissue section by lasers. It excludes transplantation, for which "transplantation" is used.']),
  NtQbin._make(['therapeutic use', 'TU', 'THER USE', 'Used with drugs, biological preparations, and physical agents for their use in the prophylaxis and treatment of disease. It includes veterinary use.']),
  NtQbin._make(['therapy', 'TH', 'THER', 'Used with diseases for therapeutic interventions except drug therapy, diet therapy, radiotherapy, and surgery, for which specific subheadings exist. The concept is also used for articles and books dealing with multiple therapies.']),
  NtQbin._make(['toxicity', 'TO', 'TOX', 'Used with drugs and chemicals for experimental human and animal studies of their ill effects. It includes studies to determine the margin of safety or the reactions accompanying administration at various dose levels. It is used also for exposure to environmental agents. Poisoning should be considered for life-threatening exposure to environmental agents.']),
  NtQbin._make(['transmission', 'TM', 'TRANSM', 'Used with diseases for studies of the modes of transmission.']),
  NtQbin._make(['transplantation', 'TR', 'TRANSPL', 'Used with organs, tissues, or cells for transplantation from one site to another within the same subject, or from one subject to another of the same species or different species.']),
  NtQbin._make(['trends', 'TD', 'TRENDS', 'Used for the manner in which a subject changes, qualitatively or quantitatively, with time, whether past, present, or future. It excludes discussions of the course of disease in particular patients.']),
  NtQbin._make(['ultrastructure', 'UL', 'ULTRASTRUCT', 'Used with tissues and cells (including neoplasms) and microorganisms for microanatomic structures, generally below the size visible by light microscopy.']),
  NtQbin._make(['urine', 'UR', 'URINE', 'Used for the presence or analysis of substances in the urine, and also for the examination of, or changes in, the urine in disease.']),
  NtQbin._make(['veterinary', 'VE', 'VET', 'Used for naturally occurring diseases in animals, or for diagnostic, preventive, or therapeutic procedures used in veterinary medicine.']),
  NtQbin._make(['virology', 'VI', 'VIROL', 'Used with organs, animals, and higher plants and with diseases for virologic studies. For bacteria, rickettsia, and fungi, "microbiology" is used; for parasites, "parasitology" is used.']),
]

# Copyright (C) 2014-2020 DV Klopfenstein. All rights reserved
