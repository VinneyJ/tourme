function deleteplace(placeId) {
  fetch("/delete-place", {
    method: "POST",
    body: JSON.stringify({ placeId: placeId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
