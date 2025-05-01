document.addEventListener("DOMContentLoaded", () => { 
    const currentElement = document.getElementsByClassName('{{rootClassName}}');
    
    if (currentElement.length > 0) {
        const labels = currentElement[0].querySelectorAll('gp-product-variants label.option-item > div:first-child > p');
        if (labels.length >= 4) {
            labels[0].innerHTML = "Um ajuste moderno e atlético, terminando <b>logo abaixo do meio da coxa.</b>";
            labels[1].innerHTML = "Para quem prefere um caimento mais tradicional, <b>ligeiramente acima do joelho.</b>";
            labels[2].innerHTML = "Perfeito para quem prioriza <b>leveza</b> e total <b>liberdade de movimento</b> durante os treinos.";
            labels[3].innerHTML = "Ideal para quem busca maior <b>estabilidade muscular</b> e prefere manter <b>itens essenciais</b> como celular e chaves <b>sempre à mão</b>, sem comprometer a mobilidade.";
        }
    }

    const tooltipTexts = [
        "O comprimento do shorts é a altura em que a peça termina na perna",
        "Indica se o shorts possui uma camada interna mais justa ao corpo, oferecendo suporte extra durante o uso.",
        "", // Ignorado
        "O comprimento do shorts é a altura em que a peça termina na perna",
        "Indica se o shorts possui uma camada interna mais justa ao corpo, oferecendo suporte extra durante o uso.",
        "" // Ignorado
    ];
    
    let spacerWidths;
    
    function updateArray() {
        if (window.innerWidth <= 768) {
            console.log("Mobile view");
            spacerWidths = ["60vw", "60vw", "0", "60vw", "60vw", "0"]; // Mobile array
        } else {
            console.log("Desktop view");
            spacerWidths = ["23vw", "20vw", "0", "23vw", "20vw", "0"]; // Desktop array
        }
        console.log(spacerWidths);
    }

    // Run initially
    updateArray();

    // Run every 1 second to check for resizing
    setInterval(updateArray, 1000);
    function createTooltip(legend, text, spacerWidth) {
        if (legend.querySelector(".tooltip-container")) return;

        const tooltipContainer = document.createElement("span");
        tooltipContainer.classList.add("tooltip-container");
        tooltipContainer.style.display = "inline-flex";
        tooltipContainer.style.alignItems = "baseline";

        const tooltip = document.createElement("b");
        tooltip.innerText = " ?";
        tooltip.classList.add("tooltip");
        tooltip.style.cursor = "pointer";
        tooltip.style.marginLeft = "5px";
        tooltip.style.position = "relative";
        tooltip.style.fontSize = "inherit";
        
        const spacer = document.createElement("span");
        spacer.style.display = "inline-block";
        spacer.style.width = spacerWidth || "10vw";

        // Adjust container height to match span
        tooltipContainer.style.height = `${spacer.offsetHeight}px`;

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
            tooltipBox.style.top = (rect.top - tooltipBox.offsetHeight - 10) + "px"; // Moves it up
            tooltipBox.style.left = (rect.left + rect.width / 2 - tooltipBox.offsetWidth / 2) + "px"; // Centers it
            tooltipBox.style.visibility = "visible";
            tooltipBox.style.opacity = "1";
        });

        tooltip.addEventListener("mouseleave", () => {
            tooltipBox.style.visibility = "hidden";
            tooltipBox.style.opacity = "0";
        });

        tooltipContainer.appendChild(spacer);
        tooltipContainer.appendChild(tooltip);
        legend.appendChild(tooltipContainer);
    }

    function updateTooltips() {
        const legends = document.querySelectorAll("legend");

        [0, 1, 3, 4].forEach(index => {
            const legend = legends[index];
            if (legend) {
                const text = tooltipTexts[index] || "Texto padrão para tooltips extras";
                const spacerWidth = spacerWidths[index] || "10vw";
                createTooltip(legend, text, spacerWidth);
            }
        });
    }

    // Run once after DOM is loaded
    updateTooltips();

    // Check every 5 seconds if the "?" is missing and restore it if necessary
    setInterval(() => {
        document.querySelectorAll("legend").forEach((legend, index) => {
            const tooltipExists = legend.querySelector(".tooltip");
            if (!tooltipExists && tooltipTexts[index]) {
                createTooltip(legend, tooltipTexts[index], spacerWidths[index]);
            }
        });
    }, 200);
    
});
