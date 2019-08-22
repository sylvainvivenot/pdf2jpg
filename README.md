# pdf2jpg

HttpResponseMessage PostFile(string url, string filePath, string parameterName)
{
  FileInfo file = new FileInfo(filePath);
  MultipartFormDataContent content = new MultipartFormDataContent("pdf");
  content.Add(new StreamContent(file.OpenRead())
  {
    Headers =
      {
        ContentLength = file.Length,
        ContentType = new MediaTypeHeaderValue("application/octet-stream"),  
      }
  }, parameterName, Path.GetFileName(filePath));

  using (HttpClient httpClient = new HttpClient())
  {
    return httpClient.PostAsync(url, content).Result;
  }
}
