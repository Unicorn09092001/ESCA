fetch("./header.html")
  .then((response) => {
    return response.text();
  })
  .then((data) => {
    document.querySelector("header").innerHTML = data;
  });

fetch("collections/footer.html")
  .then((response) => {
    return response.text();
  })
  .then((data) => {
    console.log(data);
    document.querySelector("#shopify-section-footer").innerHTML = data;
  });
