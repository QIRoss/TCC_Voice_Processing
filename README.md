# TCC_Voice_Processing

# To test voice_api in my machine:
```
curl -X POST -F "file=@/home/qiross/code/TCC/TCC_Voice_Processing/audios/smoke_inhalation_respiratory_distress.wav" http://127.0.0.1:5000/transcribe
```

```
docker build -t voice_api_image .
docker run --name voice_processing_api -d -p 5000:5000 --network host voice_api_image
```

Phrases to test Ambulance API:
"We have a patient involved in a car/motorcycle accident with injuries to the legs/arms. Suspected fractures and lacerations present."

"Patient is experiencing perfusion issues and significant blood loss. Immediate attention and blood transfusion may be required."

"Encountered a case of smoke inhalation. The patient is experiencing respiratory distress and requires urgent medical intervention."

"Multiple trauma patient with injuries to the extremities and possible internal injuries. Requesting trauma team activation upon arrival at the hospital."

"Severe chest pain reported, suspecting cardiac issues. Continuous monitoring of vital signs initiated."

"Patient with head trauma following a fall. Unconscious state observed, and pupils are unequal. Immediate neurological assessment required."

"Found a patient with signs of shock due to extensive burns. Administered fluid resuscitation, but further burn care is needed."

"Transporting a patient with a history of allergic reaction. Administered epinephrine, and the patient is stabilized but requires immediate evaluation."

"Suspected spinal injury in a patient involved in a fall. Immobilization precautions in place, and urgent imaging is recommended."

"Motor vehicle collision with entrapment. Extrication completed, and the patient is conscious but complaining of abdominal pain. Preparing for possible internal injuries."

