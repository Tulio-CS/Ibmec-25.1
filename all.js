//const currentElement = document.getElementsByClassName('{{rootClassName}}');

document.addEventListener("DOMContentLoaded", () => { 
    const currentElement = document.getElementsByClassName('{{rootClassName}}');
    
    if (currentElement.length > 0) {
        const labels = currentElement[0].querySelectorAll('gp-product-variants label.option-item > div:first-child > p');
        if (labels.length >= 4) {
            labels[2].innerHTML = "Um ajuste moderno e atlético, terminando <b>logo abaixo do meio da coxa.</b>";
            labels[3].innerHTML = "Para quem prefere um caimento mais tradicional, <b>ligeiramente acima do joelho.</b>";
            labels[4].innerHTML = "Perfeito para quem prioriza <b>leveza</b> e total <b>liberdade de movimento</b> durante os treinos.";
            labels[5].innerHTML = "Ideal para quem busca maior <b>estabilidade muscular</b> e prefere manter <b>itens essenciais</b> como celular e chaves <b>sempre à mão</b>, sem comprometer a mobilidade.";
        }
    }

    const tooltipTexts = [
    "",    
    "O comprimento do shorts é a altura em que a peça termina na perna",
    "Indica se o shorts possui uma camada interna mais justa ao corpo, oferecendo suporte extra durante o uso.", //
];
    
    function updateLegendWidths() {
    const referenceDivs = document.getElementsByClassName("gp-grid !gp-ml-0");
    if (referenceDivs.length < 1) return;

    const width = referenceDivs[0]?.clientWidth || 0;

    document.querySelectorAll("legend").forEach((legend, index) => {
        if ([1, 2].includes(index)) {
            legend.style.width = `${width}px`;
        }
        legend.style.display = "flex";
        legend.style.justifyContent = "space-between";
        legend.style.alignItems = "center";
        legend.style.visibility = "visible";
    });
    }

    function createTooltip(legend, text) {
        if (legend.querySelector(".tooltip-container")) return;

        const tooltipContainer = document.createElement("span");
        tooltipContainer.classList.add("tooltip-container");
        tooltipContainer.style.display = "inline-flex";
        tooltipContainer.style.alignItems = "center";
        tooltipContainer.style.marginLeft = "auto"; 

        const tooltip = document.createElement("b");
        tooltip.classList.add("tooltip");
        tooltip.style.cursor = "pointer";
        tooltip.style.position = "relative";
        tooltip.style.fontSize = "inherit";
        tooltip.style.fontFamily = "inherit";

        const tooltipIcon = document.createElement("img");
        tooltipIcon.src = "https://cdn.shopify.com/s/files/1/0720/1443/0436/files/questionMark.svg?v=1743907074";
        tooltipIcon.alt = "Tooltip Icon";
        tooltipIcon.style.width = "16px";
        tooltipIcon.style.height = "16px";
        tooltipIcon.style.verticalAlign = "middle";

        tooltip.appendChild(tooltipIcon);
        tooltipContainer.appendChild(tooltip);
        legend.appendChild(tooltipContainer);

        const tooltipBox = document.createElement("div");
        tooltipBox.innerText = text;
        tooltipBox.classList.add("tooltip-box");
        Object.assign(tooltipBox.style, {
            position: "fixed",
            backgroundColor: "#333",
            color: "white",
            padding: "8px 12px",
            borderRadius: "10px",
            visibility: "hidden",
            opacity: "0",
            transition: "opacity 0.1s ease-in-out",
            fontFamily: "'Gotham','sans-serif'",
            fontSize: "10px",
            zIndex: "99999",
            maxWidth: "150px",
            wordWrap: "break-word",
            whiteSpace: "normal",
        });

        const arrow = document.createElement("div");
        Object.assign(arrow.style, {
            position: "absolute",
            width: "0",
            height: "0",
            borderLeft: "6px solid transparent",
            borderRight: "6px solid transparent",
            borderTop: "6px solid #333",
            bottom: "-6px",
            left: "50%",
            transform: "translateX(-50%)"
        });

        tooltipBox.appendChild(arrow);
        document.body.appendChild(tooltipBox);

        tooltip.addEventListener("mouseenter", () => {
            const rect = tooltip.getBoundingClientRect();
            tooltipBox.style.top = (rect.top - tooltipBox.offsetHeight - 10) + "px";
            tooltipBox.style.left = (rect.left + rect.width / 2 - tooltipBox.offsetWidth / 2) + "px";
            tooltipBox.style.visibility = "visible";
            tooltipBox.style.opacity = "1";
        });

        tooltip.addEventListener("mouseleave", () => {
            tooltipBox.style.visibility = "hidden";
            tooltipBox.style.opacity = "0";
        });
    }

    function updateTooltips() {
    const legends = document.querySelectorAll("legend");

    [1, 2].forEach(index => {
        const legend = legends[index];
        if (legend) {
            const text = tooltipTexts[index] || "Texto padrão para tooltip";
            createTooltip(legend, text);
        }
    });
}

    updateLegendWidths();
    updateTooltips();

    new ResizeObserver(updateLegendWidths).observe(document.body);

    setInterval(() => {
        document.querySelectorAll("legend").forEach((legend, index) => {
            if ([0, 1, 2,3, 4].includes(index)) {
                if (!legend.style.width || legend.offsetWidth === 0) {
                    updateLegendWidths();
                }
                if (!legend.querySelector(".tooltip") && tooltipTexts[index]) {
                    createTooltip(legend, tooltipTexts[index]);
                }
            }
        });
    }, 50);
});

//const currentElement = document.getElementsByClassName('{{rootClassName}}');


