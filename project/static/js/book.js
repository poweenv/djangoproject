let currentPage = 1;
const booksPerLoad = 4;
const initialLoad = 8;
document.addEventListener("DOMContentLoaded", () => {
  function createBookElement(book) {
    let element = document.createElement("div");
    element.classList.add("book");

    element.innerHTML = `
        <img src="${book.referenceIdentifier}" alt=${book.title}>
        <div class="book-title">${book.title}</div>
        <div class="book-title">${book.creator}</div>
        <div class="book-title">${book.subjectCategory.join(",")}</div>
        `;

    return element;
  }
  function loadMoreBooks() {
    fetch(`http://api.kcisa.kr/openapi/service/rest/meta13/getKPEF0103?page=${currentPage}&books_per_load=${booksPerLoad}`)
      .then((response) => response.json())
      .then((books) => {
        let bookContainer = document.getElementById("book-container");
        books.forEach((book) => {
          let bookElement = createBookElement(book);
          bookContainer.appendChild(bookElement);
        });

        currentPage++;
      });
  }
  for (let i = 0; i < initialLoad / booksPerLoad; i++) {
    loadMoreBooks();
  }
});
