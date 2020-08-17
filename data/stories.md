## happy path
* greet
  - utter_greet
  - utter_choosetypeclassification
* mood_great
  - utter_happy

## classification path cible 1
* bloquer
  - utter_choosetypeclassification
* based_cible
  - utter_cible

## classification path cible 2
* bloquer
  - utter_choosetypeclassification
* based_cible
  - utter_cible
* not_sure
  - utter_sorryCanthelp
  - utter_choosetypeclassification

## classification path content 1
* bloquer
  - utter_choosetypeclassification
* based_content
  - utter_describe
* contient
  - action_check_existence

## classification path impact 1
* bloquer
  - utter_choosetypeclassification
* based_impact
  - utter_impact

## classification path impact 2
* bloquer
  - utter_choosetypeclassification
* based_impact
  - utter_impact
* not_sure
  - utter_sorryCanthelp
  - utter_choosetypeclassification

## path help
* help
  - utter_help

## confid
* confidentiel
  - utter_confid

## inter
* interne
  - utter_inter

## sensib
* sensible
  - utter_sensib

## diffus
* diffusable
  - utter_diffus

## sad path 1
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## thanks
* thankyou
  - utter_welcome
  - utter_goodbye

## tell_joke 1
* blagues_des_banquiers
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## tell_joke 2
* blagues_des_banquiers
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_define