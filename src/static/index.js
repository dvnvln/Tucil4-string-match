function onSubmit(event) {
    event.preventDefault();

    const form = new FormData(document.getElementById("main"));
    if (!form.get("pattern")) {
        window.alert("pattern must not empty");
        return;
    }
    if (!form.get("naskah")) {
        window.alert("naskah must not empty");
        return;
    }

    const url = getUrl(form.get("algo"));
    const req = new XMLHttpRequest();
    req.open("POST", url, true);
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const res = JSON.parse(this.response)
            populateResult(res);
        }
    }
    req.send(form);
}

function getUrl(algo) {
    let url = "/re";
    switch (algo) {
        case "bm":
            url = "/bm";
            break;
        case "kmp":
            url = "/KMP";
            break;
        case "regex":
            url = "/re";
            break;
    }
    return url;
}

function populateResult(data) {
    const result = document.getElementById("result");
    result.innerHTML = "";
    for (const item in data) {
        const dom = createItem(item, data[item]);
        result.appendChild(dom);
    }
}

function createItem(item, value) {
    const title = document.createElement("h2");
    title.innerText = item;
    const container = document.createElement("div");
    container.appendChild(title);

    for (const res of value) {
        const inner = document.createElement("div");

        const number = document.createElement("p");
        number.innerText = `Number: ${res.angka}`;
        inner.appendChild(number);

        const date = document.createElement("p");
        date.innerText = `Date: ${res.tanggal}`;
        inner.appendChild(date);

        const sentence = document.createElement("p");
        sentence.innerText = `Sentence: ${res.kalimat}`;
        inner.appendChild(sentence);

        container.appendChild(inner);
    }

    return container;
}

const form = document.getElementById("main");
form.addEventListener("submit", onSubmit);
