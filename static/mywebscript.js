let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (!request.body || typeof request.body !== "object") {
          return reply.code(400).send({ error: "Invalid request body" });
        }
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").textContent = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
