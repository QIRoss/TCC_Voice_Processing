# TCC_Voice_Processing

# To test voice_api in my machine:
```
curl -X POST -F "file=@/home/qiross/code/TCC/TCC_Voice_Processing/audios/smoke_inhalation_respiratory_distress.wav" http://127.0.0.1:5000/transcribe
```

```
docker build -t voice_api_image .
docker run --name voice_processing_api -d -p 5000:5000 --network host voice_api_image
```