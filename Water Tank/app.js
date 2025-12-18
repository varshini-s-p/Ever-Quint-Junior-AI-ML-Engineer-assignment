// app.js - Vanilla JS implementation
(() => {
  const heightsInput = document.getElementById('heights');
  const runBtn = document.getElementById('runBtn');
  const resetBtn = document.getElementById('resetBtn');
  const sampleBtn = document.getElementById('sampleBtn');
  const totalEl = document.getElementById('totalWater');
  const blockCountEl = document.getElementById('blockCount');
  const svgWrap = document.getElementById('svgWrap');
  const tableWrap = document.getElementById('tableWrap');

  const SAMPLES = [
    {name: 'Sample 1', arr: [3,0,2,0,4], expected: 7},
    {name: 'Sample 2', arr: [0,1,0,2,1,0,1,3,2,1,2,1], expected: 6},
    {name: 'Flat', arr: [1,1,1,1], expected: 0},
  ];

  function parseInput(raw) {
    if (!raw) return [];
    const tokens = raw.split(/[\s,]+/).filter(Boolean);
    const vals = tokens.map(t => {
      const v = parseInt(t, 10);
      return Number.isNaN(v) ? null : v;
    });
    if (vals.some(v => v === null)) throw new Error('Invalid input: only integers allowed');
    return vals;
  }

  function computeWaterPerIndex(heights) {
    const n = heights.length;
    if (n === 0) return {total: 0, water: []};
    const leftMax = new Array(n);
    const rightMax = new Array(n);
    leftMax[0] = heights[0];
    for (let i = 1; i < n; i++) leftMax[i] = Math.max(leftMax[i-1], heights[i]);
    rightMax[n-1] = heights[n-1];
    for (let i = n-2; i >= 0; i--) rightMax[i] = Math.max(rightMax[i+1], heights[i]);
    const water = new Array(n).fill(0);
    let total = 0;
    for (let i = 0; i < n; i++) {
      const w = Math.max(0, Math.min(leftMax[i], rightMax[i]) - heights[i]);
      water[i] = w;
      total += w;
    }
    return {total, water, leftMax, rightMax};
  }

  function drawSVG(heights, water) {
    svgWrap.innerHTML = ''; // clear
    const n = heights.length;
    if (n === 0) {
      svgWrap.innerHTML = '<div style="padding:12px;color:#6b7280">No data to display.</div>';
      return;
    }

    const maxH = Math.max(...heights, ...water.map((w,i)=>heights[i]+w));
    const cols = n;
    const padding = 12;
    const width = 800; // svg viewport width (CSS will scale)
    const height = Math.max(200, Math.min(600, 30 * (maxH + 2)));

    const colW = Math.floor((width - padding*2) / (cols || 1));
    const blockGap = Math.max(2, Math.floor(colW * 0.12));
    const rectW = Math.max(6, colW - blockGap);

    const svgNS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNS, 'svg');
    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');

    // baseline at bottom with margin
    const baseline = height - 20;

    // scale factor: 1 height unit => pixels
    const pxPerUnit = (baseline - 20) / Math.max(1, maxH);

    // draw gridlines and y axis ticks
    for (let u = 0; u <= maxH; u++) {
      const y = baseline - u * pxPerUnit;
      const line = document.createElementNS(svgNS, 'line');
      line.setAttribute('x1', padding);
      line.setAttribute('x2', width - padding);
      line.setAttribute('y1', y);
      line.setAttribute('y2', y);
      line.setAttribute('stroke', '#eef2ff');
      line.setAttribute('stroke-width', u % 5 === 0 ? 1 : 0.5);
      svg.appendChild(line);

      if (u % 5 === 0) {
        const txt = document.createElementNS(svgNS, 'text');
        txt.setAttribute('x', 6);
        txt.setAttribute('y', y - 2);
        txt.setAttribute('class', 'axis-text');
        txt.textContent = u;
        svg.appendChild(txt);
      }
    }

    // draw each block and water
    for (let i = 0; i < n; i++) {
      const x = padding + i * colW + blockGap/2;
      const bh = heights[i];
      const hw = rectW;
      const blockTop = baseline - bh * pxPerUnit;
      const blockH = bh * pxPerUnit;

      // block rectangle
      const blockRect = document.createElementNS(svgNS, 'rect');
      blockRect.setAttribute('x', x);
      blockRect.setAttribute('y', blockTop);
      blockRect.setAttribute('width', hw);
      blockRect.setAttribute('height', blockH);
      blockRect.setAttribute('rx', Math.max(1, hw * 0.12));
      blockRect.setAttribute('class', 'block-rect');
      svg.appendChild(blockRect);

      // water rectangle (if any)
      const w = water[i] || 0;
      if (w > 0) {
        const waterTop = blockTop - w * pxPerUnit;
        const waterRect = document.createElementNS(svgNS, 'rect');
        waterRect.setAttribute('x', x);
        waterRect.setAttribute('y', waterTop);
        waterRect.setAttribute('width', hw);
        waterRect.setAttribute('height', w * pxPerUnit);
        waterRect.setAttribute('class', 'water-rect');
        svg.appendChild(waterRect);
      }

      // index label
      const idxTxt = document.createElementNS(svgNS, 'text');
      idxTxt.setAttribute('x', x + hw/2);
      idxTxt.setAttribute('y', baseline + 14);
      idxTxt.setAttribute('class', 'axis-text');
      idxTxt.setAttribute('text-anchor', 'middle');
      idxTxt.textContent = i;
      svg.appendChild(idxTxt);

      // height label
      const hTxt = document.createElementNS(svgNS, 'text');
      hTxt.setAttribute('x', x + hw/2);
      hTxt.setAttribute('y', blockTop - 6);
      hTxt.setAttribute('class', 'axis-text');
      hTxt.setAttribute('text-anchor', 'middle');
      hTxt.textContent = heights[i];
      svg.appendChild(hTxt);
    }

    svgWrap.appendChild(svg);
  }

  function drawTable(heights, water) {
    tableWrap.innerHTML = '';
    if (heights.length === 0) return;
    const table = document.createElement('table');
    table.style.width = '100%';
    table.style.borderCollapse = 'collapse';

    const headerRow = document.createElement('tr');
    ['Index', 'Height', 'Water at index'].forEach(h => {
      const th = document.createElement('th');
      th.style.textAlign = 'left';
      th.style.padding = '6px 8px';
      th.style.borderBottom = '1px solid #e6edf3';
      th.textContent = h;
      headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

    for (let i = 0; i < heights.length; i++) {
      const row = document.createElement('tr');
      [i, heights[i], water[i] || 0].forEach(c => {
        const td = document.createElement('td');
        td.style.padding = '6px 8px';
        td.textContent = c;
        row.appendChild(td);
      });
      table.appendChild(row);
    }

    tableWrap.appendChild(table);
  }

  function updateUI(heights) {
    try {
      const { total, water } = computeWaterPerIndex(heights);
      totalEl.textContent = total;
      blockCountEl.textContent = heights.length;
      drawSVG(heights, water);
      drawTable(heights, water);
    } catch (err) {
      svgWrap.innerHTML = `<div style="padding:12px;color:#f43f5e">Error: ${err.message}</div>`;
      tableWrap.innerHTML = '';
    }
  }

  // Wire events
  runBtn.addEventListener('click', () => {
    try {
      const heights = parseInput(heightsInput.value);
      updateUI(heights);
    } catch (err) {
      alert(err.message);
    }
  });

  resetBtn.addEventListener('click', () => {
    heightsInput.value = '';
    totalEl.textContent = '0';
    blockCountEl.textContent = '0';
    svgWrap.innerHTML = '';
    tableWrap.innerHTML = '';
  });

  sampleBtn.addEventListener('click', () => {
    const sample = SAMPLES[0]; // default pick first
    heightsInput.value = sample.arr.join(', ');
    updateUI(sample.arr);
  });

  // optional: run a default sample on load
  window.addEventListener('load', () => {
    heightsInput.value = SAMPLES[1].arr.join(', ');
    updateUI(SAMPLES[1].arr);
  });

  // export for simple test usage in console
  window._wt_utils = { parseInput, computeWaterPerIndex };
})();
