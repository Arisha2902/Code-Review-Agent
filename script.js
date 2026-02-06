// async function reviewPR() {
//   const prUrl = document.getElementById("prUrl").value;
//   const output = document.getElementById("output");

//   if (!prUrl) {
//     alert("Please enter a GitHub PR URL");
//     return;
//   }

//   output.innerHTML = `<div class="card">🔍 Analyzing Pull Request...</div>`;

//   try {
//     const response = await fetch("http://127.0.0.1:8000/review-pr", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ pr_url: prUrl })
//     });

//     const data = await response.json();
//     renderResult(data.review);
//   } catch (err) {
//     output.innerHTML = `<div class="card">❌ Backend error</div>`;
//   }
// }

// function renderResult(text) {
//   const output = document.getElementById("output");

//   const score = parseInt((text.match(/Risk Score:\s*(\d+)/) || [0,0])[1]);
//   const decision =
//     text.includes("Safe to Merge") ? "Safe to Merge" :
//     text.includes("Review Carefully") ? "Review Carefully" :
//     "Do Not Merge";

//   let colorClass = score <= 30 ? "safe" : score <= 70 ? "warn" : "danger";

//   output.innerHTML = `
//     <div class="card">
//       <div class="risk-meter">
//         <div class="circle ${colorClass}">
//           ${score}
//         </div>
//         <div class="bar">
//           <h2>${decision}</h2>
//           <div class="progress">
//             <div class="progress-fill ${colorClass}" style="width:${score}%"></div>
//           </div>
//         </div>
//       </div>
//     </div>

//     <details class="card">
//       <summary>🔴 Critical Issues</summary>
//       <pre>${extract(text, "Critical Issues")}</pre>
//     </details>

//     <details class="card">
//       <summary>🟡 Medium Issues</summary>
//       <pre>${extract(text, "Medium")}</pre>
//     </details>

//     <details class="card">
//       <summary>🟢 Minor Suggestions</summary>
//       <pre>${extract(text, "Minor")}</pre>
//     </details>
//   `;
// }

// // function extract(text, key) {
// //   const part = text.split(key)[1];
// //   return part ? part.split("###")[0].trim() : "None";
// // }

// function extract(text, section) {
//   const regex = new RegExp(`###\\s*${section}[\\s\\S]*?(?=###|$)`, "i");
//   const match = text.match(regex);
//   return match ? match[0].replace(/###.*\n/, "").trim() : "None";
// }

async function reviewPR() {
  const prUrl = document.getElementById("prUrl").value;
  const output = document.getElementById("output");

  if (!prUrl) {
    alert("Please enter a GitHub Pull Request URL");
    return;
  }

  output.innerHTML = `
    <div class="card">
      🔍 Analyzing Pull Request… <br/>
      <small>This may take a few seconds</small>
    </div>
  `;

  try {
    const response = await fetch("http://127.0.0.1:8000/review-pr", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pr_url: prUrl })
    });

    if (!response.ok) {
      throw new Error("Backend error");
    }

    const data = await response.json();
    renderResult(data.review);

  } catch (err) {
    console.error(err);
    output.innerHTML = `
      <div class="card">
        ❌ Failed to analyze PR.<br/>
        <small>Check backend logs or GitHub token.</small>
      </div>
    `;
  }
}

function renderResult(text) {
  const output = document.getElementById("output");

  // ---- Risk Score ----
  const scoreMatch = text.match(/Risk Score:\s*(\d+)/i);
  const score = scoreMatch ? parseInt(scoreMatch[1]) : 0;

  // ---- Decision ----
  let decision = "Review Carefully";
  if (/Safe to Merge/i.test(text)) decision = "Safe to Merge";
  if (/Do Not Merge/i.test(text)) decision = "Do Not Merge";

  // ---- Color Logic ----
  let colorClass = "warn";
  if (score <= 30) colorClass = "safe";
  else if (score >= 71) colorClass = "danger";

  output.innerHTML = `
    <div class="card">
      <div class="risk-meter">
        <div class="circle ${colorClass}">
          ${score}
        </div>
        <div class="bar">
          <h2>${decision}</h2>
          <div class="progress">
            <div class="progress-fill ${colorClass}" style="width:${score}%"></div>
          </div>
        </div>
      </div>
    </div>

    <details class="card" open>
      <summary>🔴 Critical Issues</summary>
      <pre>${extractSection(text, "Critical Issues")}</pre>
    </details>

    <details class="card">
      <summary>🟡 Medium Priority Issues</summary>
      <pre>${extractSection(text, "Medium Priority Issues")}</pre>
    </details>

    <details class="card">
      <summary>🟢 Minor Suggestions</summary>
      <pre>${extractSection(text, "Minor Suggestions")}</pre>
    </details>
  `;
}

function extractSection(text, sectionTitle) {
  const regex = new RegExp(
    `###\\s*${sectionTitle}[\\s\\S]*?(?=###|$)`,
    "i"
  );

  const match = text.match(regex);
  if (!match) return "None";

  return match[0]
    .replace(new RegExp(`###\\s*${sectionTitle}`, "i"), "")
    .trim() || "None";
}


