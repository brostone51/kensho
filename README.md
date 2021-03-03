# kensho

As of my push at ~7:30, it parses through the pages super well and arrives at results pretty quickly, even in my VM where the process is a bit limited.
However, the results aren't matching what the wikipedia page says should happen. Something is likely to be wrong with my `get_first_anchor` function.

### update

Was able to make it better, but only somewhat. There seems to be something wrong with my link finding function, but I'm not sure what. According to the sample pages I am actually viewing, it should be accurately grabbing the first link from the page. But based on the ratio I'm seeing in outuput, either this article is no longer true or something is up.

At any rate, I am pretty much out of time here. I wish I could figure out why I'm getting the wrong link, but it still succesffuly parses the link chains and does some pruning when it knows it going to fail.

Here is a sample output:

```text
Loop Failure:  Takht_Bhai_Tehsil -> Tehsil -> Administrative_division -> Sovereign_state -> Political_entity -> Collective_identity -> Belongingness -> Emotional -> Biological -> Natural_science -> Branches_of_science -> Science -> Latin -> Classical_language -> Language -> Spoken_language -> Language
Failure:  FYI_(Canadian_TV_channel) -> Television_in_Canada -> Montreal -> Help:Pronunciation_respelling_key -> Pronunciation_respelling_for_English -> Pronunciation_respelling -> Nonce_word -> Lexeme -> Lexical_semantics -> Linguistics -> Science
Failure:  Cydia_strobilella -> Moth -> Paraphyly -> Taxonomy_(general) -> Categorization -> Experience -> Consciousness -> Sentience -> Feeling -> Nominalization -> Linguistics
~~~ Path Found:  Pandero_jarocho -> Tambourine -> Musical_instrument -> Music -> The_arts -> Creativity -> Idea -> Philosophy
Failure:  David_Hartley_(musician) -> Sting_(musician) -> Order_of_the_British_Empire -> Order_of_chivalry -> Order_(honour) -> Honour -> British_English -> Standard_dialect -> Variety_(linguistics) -> Sociolinguistics -> Society -> Social_group -> Social_science -> Branches_of_science
Loop Failure:  Old_Adobe_Barn -> Historic -> Ancient_Greek -> Greek_language -> Ancient_Greek
Failure:  Samuel_Curtis_Johnson_Graduate_School_of_Management -> Graduate_school -> School -> Educational_institution -> Education -> Learning -> Understanding -> Psychological -> Science
Failure:  Leon_Burke_III -> St._Louis,_Missouri -> Missouri -> U.S._state -> United_States -> Country -> Territory -> Administrative_division
~~~ Path Found:  Szczepan_Grajczyk -> Rowing_(sport) -> Sport -> Competition -> Goal -> Idea -> Philosophy
~~~ Path Found:  Charles_Lowe_(cricketer) -> Cricket -> Bat-and-ball_games -> Playing_field -> Sport -> Competition -> Goal -> Idea -> Philosophy
Failure:  Erebia_lefebvrei -> Satyridae -> Subfamily -> Biological_classification -> Biology -> Natural_science
Failure:  Gal_Rasch%C3%A9 -> Saint_Petersburg -> List_of_cities_and_towns_in_Russia_by_population -> Types_of_inhabited_localities_in_Russia -> Soviet_Union -> Federalism -> Government -> State_(polity) -> Polity -> Collective_identity
Failure:  Mollie_Lowery -> Los_Angeles -> Spanish_language -> Romance_languages -> Vulgar_Latin -> Sociolect -> Sociolinguistics
Failure:  2005_European_Athletics_Indoor_Championships_%E2%80%93_Women%27s_3000_metres -> 2005_European_Athletics_Indoor_Championships -> Palacio_de_Deportes_de_la_Comunidad_de_Madrid -> Indoor_arena -> Theatre -> Performing_art -> Visual_arts -> Art#Forms,_genres,_media,_and_styles -> Human_behavior -> Energy_(psychological) -> Psychology -> Science
Failure:  Faiyum_Light_Railway -> 750_mm_gauge_railways -> Narrow-gauge_railway -> Railway -> Transport -> Motion -> Physics -> Ancient_Greek_language -> Greek_language
Failure:  Jennifer_Hines -> Opera_singer -> Theatre
Failure:  Tris(8-hydroxyquinolinato)aluminium -> Chemical_compound -> Chemical_substance -> Matter -> Classical_physics -> Physics
Failure:  Wilton_Windmill -> Windmill -> Wind_power -> Wind -> Gas -> State_of_matter -> Physics
Failure:  Manolo_Garc%C3%ADa -> Poblenou -> Catalan_language -> Endonym -> Greek_language
Failure:  Yunganglong -> Extinct -> Organism -> Biology
Failure:  Lie%C5%A1%C5%A5any -> Hungarian_language -> Uralic_language -> Language_family -> Language
Failure:  Walsingham_Rural_District -> Rural_district -> Local_government -> Public_administration -> Public_policy -> Government
Failure:  Pranav_Sivakumar -> United_States
Failure:  List_of_statues_in_Yerevan -> Yerevan -> Help:Pronunciation_respelling_key
Failure:  Legal_treatise -> Legal_publication -> Book -> Information -> Uncertainty -> Epistemology -> Greek_language
Failure:  New_South_Wales_Typographical_Association -> Australia -> Sovereign_state
Failure:  King_of_Romania -> Romanian_language -> Balkan_Romance_languages -> Romance_languages
Failure:  K_College -> Further_education -> United_Kingdom -> Sovereign_state
Failure:  Brittin
Failure:  Daehaeng -> Korean_Seon -> Korean_language -> Languages_of_East_Asia -> Language_families -> Language
Failure:  Spaccacuore -> Samuele_Bersani -> Rimini -> Help:Pronunciation_respelling_key
Failure:  Linari
Failure:  Semper_Femina -> Laura_Marling -> Folk_music -> Folk_revival -> Josh_White -> Southern_United_States -> List_of_regions_of_the_United_States#Official_regions_of_the_United_States -> Office_of_Management_and_Budget -> Executive_Office_of_the_President_of_the_United_States -> List_of_federal_agencies_in_the_United_States -> Government_agency -> Machinery_of_government -> Government
Failure:  Barter_Theatre -> Abingdon,_Virginia -> Town -> Human_settlement -> Geography -> Ancient_Greek
Failure:  2000%E2%80%9301_Slovenian_PrvaLiga
Failure:  Vemulapally,_Telangana -> Nalgonda_district -> District -> Administrative_division
Failure:  Acrocercops_melantherella -> Moth
Failure:  The_Shepherd%27s_Life -> James_Rebanks -> Matterdale -> Civil_parishes_in_England -> Parish_(administrative_division) -> Administrative_division
Failure:  Ptolemaic_graph -> Graph_theory -> Mathematics -> Ancient_Greek
~~~ Path Found:  Luiz_Ot%C3%A1vio -> Association_football -> Team_sport -> Sport -> Competition -> Goal -> Idea -> Philosophy
Failure:  Chiuzbaia -> Hungarian_language
Loop Failure:  Haematococcus_pluvialis -> Chlorophyta -> Prasinophyte -> Tetraphytina -> Chlorophyta
Loop Failure:  Kirkton,_Dundee -> Dundee -> Scots_language -> Scottish_Gaelic_language -> Scottish_Gaelic_language
Failure:  List_of_GetBackers_characters -> Germans -> German_language -> West_Germanic_languages -> Germanic_languages -> Indo-European_languages -> Language_family
Failure:  The_Private_Lives_of_Elizabeth_and_Essex -> Historical_drama -> Historical_fiction -> Setting_(narrative) -> Time -> Sequence -> Mathematics
Failure:  Children,_Go_Where_I_Send_Thee -> African-American -> Ethnic_group -> Identity_(social_science) -> Self-identity -> Belief -> Attitude_(psychology) -> Psychology
~~~ Path Found:  Marcelino_Solis -> Professional_baseball -> Baseball -> Bat-and-ball_games -> Playing_field -> Sport -> Competition -> Goal -> Idea -> Philosophy
Failure:  Radomierowice -> German_language
Failure:  Lansdowne,_India -> Cantonment -> French_language -> Romance_languages
Failure:  Wollensak -> United_States
Failure:  List_of_selective_high_schools_in_New_South_Wales -> Selective_High_Schools_Test -> New_South_Wales -> States_and_territories_of_Australia -> Australia
Failure:  Grameen_Bank -> Bengali_language -> Endonym
Failure:  Fred_Quine -> Australia
Failure:  Tassie_(surname)
Failure:  Mukden_Arsenal_Mauser -> Mauser_Model_1904#Chinese_variants -> Gewehr_98 -> Bolt_action -> Firearm_action -> Firearms -> Gun -> Ranged_weapon -> Weapon -> Hunting -> Wildlife -> Animal -> Multicellular -> Organism
Failure:  Jamestown,_California -> Census-designated_place -> Place_(United_States_Census_Bureau) -> United_States_Census_Bureau -> Federal_Statistical_System_of_the_United_States -> Federal_government_of_the_united_states -> Federation#Federal_governments -> Political_entity
Failure:  Magalang -> Kapampangan_language -> Austronesian_language -> Language_family
Loop Failure:  Mary_of_Egypt -> Coptic_language -> Egyptian_language -> Coptic_language
Failure:  Roman_Catholic_Diocese_of_Modigliana -> Roman_Catholic -> List_of_Christian_denominations_by_number_of_members -> Christian_denomination -> Religion -> Social_system -> Sociology -> Society
Failure:  Tom_Mix -> Western_(genre) -> Genre -> French_language
Failure:  Join_or_Die_with_Craig_Ferguson -> Panel_show -> Radio_broadcasting -> Audio_signal -> Sound -> Physics
Failure:  Jes%C3%BAs_Baldaccini -> Argentinian_people -> Spanish_language
~~~ Path Found:  1987%E2%80%9388_Ranji_Trophy -> Ranji_Trophy -> First-class_cricket -> Cricket -> Bat-and-ball_games -> Playing_field -> Sport -> Competition -> Goal -> Idea -> Philosophy
Failure:  Karoo_Moose -> South_Africa -> Africa -> Continent -> Landmass -> Region -> Geography
Failure:  Labdia_tristoecha -> Moth
Failure:  Jalali_(tribe) -> Persian_language -> Exonym_and_endonym -> Greek_language
Failure:  Canton_of_Toulouse-3 -> Haute-Garonne -> Occitan_language -> French_language
Failure:  Les_Cerqueux-sous-Passavant -> Communes_of_France -> Administrative_divisions -> Sovereign_state
Failure:  Connor_Hotel_(Joplin,_Missouri) -> Beaux-Arts_architecture -> Architectural_style -> Style_(visual_arts) -> Visual_arts
Failure:  Cape_dory -> Indian_Ocean -> Ocean -> Water -> Inorganic_compound -> Chemical_compound
Failure:  Lipoteichoic_acid -> Cell_wall -> Cell_(biology) -> Latin
Loop Failure:  Don_%22Magic%22_Juan -> Pimp -> Prostitute -> Human_sexual_activity -> Human_sexuality -> Human_sexual_activity
Failure:  Lane_DeGregory -> St._Petersburg_Times -> Newspaper -> Periodical_literature -> Serial_(publishing) -> Publishing -> Book
Failure:  Heinrich_von_W%C3%BClzburg -> Germany -> German_language
Failure:  Ingo_Haar -> Germans
Failure:  Generalov -> Russian_language -> East_Slavic_languages -> Slavic_languages -> Indo-European_languages
Failure:  Worleston -> Civil_parishes_in_England
Failure:  Woodstock_1994_(Red_Hot_Chili_Peppers_album) -> Bootleg_recording -> Sound_recording -> Electrical -> Physics
Failure:  %C3%86thelweald -> Bishop_of_Dunwich_(ancient) -> Episcopal_polity -> Hierarchy -> Ancient_Greek
Failure:  Theodore_I_Laskaris -> Greek_language
Failure:  Silliman_Institute -> Segregation_academy -> Private_school -> Non-governmental -> Organization -> English_in_the_Commonwealth_of_Nations -> English_language -> West_Germanic_languages
Failure:  Corona_(satellite) -> United_States
~~~ Path Found:  2008_Australian_Manufacturers%27_Championship -> Confederation_of_Australian_Motor_Sport -> Motor_sport -> Sports -> Competition -> Goal -> Idea -> Philosophy
Failure:  Pageant_(album) -> PWR_BTTM -> Queer -> Umbrella_term -> Linguistics
Failure:  Muthomi_Njuki -> Tharaka_Nithi_County -> Counties_of_Kenya -> Swahili_language -> Bantu_languages -> Language_family
Failure:  Shamchaurasi -> Municipal_council -> Legislature -> Deliberative_assembly -> Collective -> Cooperative -> Autonomy -> Developmental_psychology -> Science
Failure:  First_United_Lutheran_Church -> Evangelical_Lutheran_Church_in_America -> Mainline_Protestant -> Protestantism_in_the_United_States -> Protestantism -> Christianity -> Abrahamic_religions -> Semitic_people -> Historical_race_concepts -> Race_(classification_of_human_beings) -> Human -> Species -> Biology
Failure:  Organa_(crater) -> Impact_crater -> Depression_(geology) -> Geology -> Ancient_Greek
Failure:  Pleurodontagama -> Genus -> Taxonomic_rank -> Biological_classification
Failure:  Cloudera -> United_States
Failure:  Robert_Lehman -> United_States
Failure:  Pierre-Antoine_Antonelle -> Jacobin_Club -> French_language
Failure:  Head_of_the_Prime_Minister%27s_military_cabinet -> Military_of_France -> French_language
Failure:  Lior%C3%A9_et_Olivier_LeO_20 -> France -> Western_Europe -> Europe -> Continent
Failure:  James_M._Ideman -> United_States_federal_judge -> United_States
Failure:  Seilbahn_Zugspitze -> Zugspitze -> Normalh%C3%B6hennull -> Vertical_datum -> Vertical_position -> Position_(mathematics) -> Geometry -> Ancient_Greek_language
Failure:  Girl_Asleep_(film) -> Surrealist_film -> Dada -> Art_movement -> Art -> Human_behavior
Failure:  John_Wright_(Missouri_politician) -> Missouri_House_of_Representatives -> Missouri_General_Assembly -> State_legislature_(United_States) -> United_States
Failure:  Canton_of_Sault -> France
Failure:  List_of_radio_stations_in_Northern_Region -> Ghana -> Gulf_of_Guinea -> Atlantic_Ocean -> Ocean
Passes:  7
Fails:  93
Longest path:  12

Frequencies of the last page in the chain:
Language :  3
Science :  4
Linguistics :  2
Philosophy :  7
Branches_of_science :  1
Ancient_Greek :  5
Administrative_division :  3
Natural_science :  1
Collective_identity :  1
Sociolinguistics :  1
Greek_language :  5
Theatre :  1
Physics :  4
Biology :  2
Government :  2
United_States :  7
Help:Pronunciation_respelling_key :  2
Sovereign_state :  3
Romance_languages :  2
Brittin :  1
Linari :  1
2000%E2%80%9301_Slovenian_PrvaLiga :  1
Moth :  2
Hungarian_language :  1
Chlorophyta :  1
Scottish_Gaelic_language :  1
Language_family :  3
Mathematics :  1
Psychology :  1
German_language :  2
Australia :  2
Endonym :  1
Tassie_(surname) :  1
Organism :  1
Political_entity :  1
Coptic_language :  1
Society :  1
French_language :  4
Spanish_language :  1
Geography :  1
Visual_arts :  1
Chemical_compound :  1
Latin :  1
Human_sexual_activity :  1
Book :  1
Germans :  1
Indo-European_languages :  1
Civil_parishes_in_England :  1
West_Germanic_languages :  1
Biological_classification :  1
Continent :  1
Ancient_Greek_language :  1
Human_behavior :  1
France :  1
Ocean :  1

```
