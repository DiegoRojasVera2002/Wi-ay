<script>
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import {
    getProject,
    getProjectSteps,
    enrollInProject,
    submitCode,
    getUser,
  } from "$lib/api";

  let projectId;
  let project = null;
  let steps = [];
  let currentStep = 0;
  let loading = true;
  let user = null;
  let code = "";
  let submitting = false;
  let result = null;
  let showCelebration = false;
  let shakeError = false;

  $: projectId = $page.params.id;
  $: progress = steps.length > 0 ? ((currentStep + 1) / steps.length) * 100 : 0;

  onMount(async () => {
    user = getUser();

    try {
      project = await getProject(projectId);
      steps = await getProjectSteps(projectId);

      // Auto-enroll if logged in
      if (user) {
        try {
          await enrollInProject(projectId, user.id);
        } catch (err) {
          // Already enrolled, ignore
        }
      }
    } catch (err) {
      console.error("Error:", err);
    } finally {
      loading = false;
    }
  });

  async function handleSubmit() {
    if (!user) {
      alert("Debes iniciar sesión para enviar código");
      return;
    }

    if (!code.trim()) {
      return;
    }

    submitting = true;
    result = null;
    showCelebration = false;
    shakeError = false;

    try {
      const submission = await submitCode(steps[currentStep].id, code, user.id);
      result = JSON.parse(submission.test_results);

      // Show celebration or shake animation
      if (result.status === "passed") {
        showCelebration = true;
        setTimeout(() => {
          showCelebration = false;
        }, 3000);
      } else {
        shakeError = true;
        setTimeout(() => {
          shakeError = false;
        }, 500);
      }
    } catch (err) {
      alert("Error al enviar código: " + err.message);
      shakeError = true;
      setTimeout(() => {
        shakeError = false;
      }, 500);
    } finally {
      submitting = false;
    }
  }

  function nextStep() {
    if (currentStep < steps.length - 1) {
      currentStep++;
      code = "";
      result = null;
      showCelebration = false;
    }
  }

  function prevStep() {
    if (currentStep > 0) {
      currentStep--;
      code = "";
      result = null;
      showCelebration = false;
    }
  }

  function exitLesson() {
    if (confirm("¿Seguro que quieres salir? Tu progreso se guardará.")) {
      window.location.href = "/modules";
    }
  }
</script>

<svelte:head>
  <title>{project?.title || "Proyecto"} - Wiñay</title>
</svelte:head>

<!-- CELEBRATION CONFETTI -->
{#if showCelebration}
  <div class="celebration-overlay">
    <div class="celebration-content">
      <div class="celebration-icon">🎉</div>
      <h2>¡Increíble!</h2>
      <p>Todos los tests pasaron</p>
    </div>
  </div>
{/if}

<div class="lesson-page-duo">
  {#if loading}
    <div class="loading-lesson">
      <div class="loading-spinner">🔄</div>
      <p>Cargando proyecto...</p>
    </div>
  {:else if !project}
    <div class="container">
      <div class="error-message-duo">
        <div class="error-icon">😕</div>
        <h3>Proyecto no encontrado</h3>
        <a href="/modules" class="btn-primary">VOLVER A MÓDULOS</a>
      </div>
    </div>
  {:else}
    <!-- TOP BAR WITH PROGRESS -->
    <div class="lesson-topbar">
      <button class="btn-exit" on:click={exitLesson}>✕</button>

      <div class="progress-container">
        <div class="progress-bar-lesson">
          <div class="progress-fill-lesson" style="width: {progress}%"></div>
        </div>
      </div>

      <div class="topbar-info">
        <div class="company-badge">🏢 {project.company_name}</div>
      </div>
    </div>

    <!-- MAIN LESSON CONTENT - TWO COLUMN LAYOUT LIKE DATACAMP -->
    <div class="lesson-container-split">
      {#if steps.length > 0}
        <!-- LEFT COLUMN: Instructions -->
        <div class="left-panel">
          <div class="instructions-scroll">
            <!-- Step indicator with XP -->
            <div class="step-header">
              <span class="step-label"
                >Paso {currentStep + 1} de {steps.length}</span
              >
              <div class="xp-badge">
                <span class="xp-icon">⭐</span>
                <span>+100 XP</span>
              </div>
            </div>

            <!-- Task title and description -->
            <div class="task-content">
              <h1 class="task-title">{steps[currentStep].title}</h1>
              <div class="task-description">
                {@html steps[currentStep].content.replace(/\n/g, "<br>")}
              </div>
            </div>

            <!-- Hint button -->
            <div class="hint-section">
              <button class="btn-hint" disabled>
                <span class="hint-icon">💡</span>
                <span>Take Hint</span>
                <span class="hint-cost">(-30 XP)</span>
              </button>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: Code Editor & Results -->
        <div class="right-panel">
          <div class="editor-scroll" class:shake-animation={shakeError}>
            <!-- Code editor section -->
            <div class="code-section-duo">
              <div class="code-header">
                <span class="code-icon">�</span>
                <span class="code-label">script.py</span>
              </div>
              <textarea
                bind:value={code}
                placeholder="def solution(data):&#10;    # Tu código aquí&#10;    return resultado"
                class="code-textarea-duo"
                rows="18"
              ></textarea>
            </div>

            <!-- Result feedback -->
            {#if result}
              <div
                class="result-feedback-duo"
                class:success={result.status === "passed"}
                class:error={result.status !== "passed"}
              >
                <div class="result-header-duo">
                  {#if result.status === "passed"}
                    <div class="result-icon success-icon">✓</div>
                    <div class="result-text">
                      <h3>¡Perfecto!</h3>
                      <p>Todos los tests pasaron correctamente</p>
                    </div>
                  {:else}
                    <div class="result-icon error-icon">✗</div>
                    <div class="result-text">
                      <h3>Intenta de nuevo</h3>
                      <p>Algunos tests no pasaron. Revisa tu código</p>
                    </div>
                  {/if}
                </div>

                <div class="tests-summary">
                  <div class="test-score">
                    {result.passed}/{result.total} tests pasados
                  </div>
                </div>

                {#if result.results && result.results.length > 0}
                  <div class="test-list-duo">
                    {#each result.results as test}
                      <div
                        class="test-row-duo"
                        class:passed={test.status === "passed"}
                      >
                        <span class="test-check"
                          >{test.status === "passed" ? "✓" : "✗"}</span
                        >
                        <span class="test-name">Test {test.test}</span>
                        {#if test.expected}
                          <div class="test-details">
                            <span class="expected"
                              >Esperado: {test.expected}</span
                            >
                            <span class="got">Obtenido: {test.got}</span>
                          </div>
                        {/if}
                      </div>
                    {/each}
                  </div>
                {/if}

                {#if result.error}
                  <div class="error-code">
                    <pre>{result.error}</pre>
                  </div>
                {/if}
              </div>
            {/if}
          </div>
        </div>
      {/if}
    </div>

    <!-- BOTTOM BAR WITH CHECK BUTTON (DUOLINGO STYLE) -->
    <div class="lesson-bottombar">
      <div class="bottombar-content">
        {#if result && result.status === "passed"}
          <!-- Show CONTINUE button if passed -->
          <button
            class="btn-lesson-duo btn-continue"
            on:click={nextStep}
            disabled={currentStep === steps.length - 1}
          >
            {currentStep === steps.length - 1 ? "¡COMPLETADO!" : "CONTINUAR"}
          </button>
        {:else}
          <!-- Show CHECK button -->
          <button
            class="btn-lesson-duo btn-check"
            on:click={handleSubmit}
            disabled={submitting || !code.trim()}
          >
            {submitting ? "COMPROBANDO..." : "COMPROBAR"}
          </button>
        {/if}
      </div>
    </div>
  {/if}
</div>

<style>
  /* LESSON PAGE LAYOUT */
  .lesson-page-duo {
    min-height: 100vh;
    background: #f8f9fa;
    display: flex;
    flex-direction: column;
  }

  /* TWO COLUMN LAYOUT LIKE DATACAMP */
  .lesson-container-split {
    display: grid;
    grid-template-columns: 45% 55%;
    flex: 1;
    overflow: hidden;
    background: white;
  }

  /* LEFT PANEL - Instructions */
  .left-panel {
    background: white;
    border-right: 1px solid var(--gray-200);
    overflow-y: auto;
    height: calc(100vh - 80px);
  }

  .instructions-scroll {
    padding: 40px;
    max-width: 700px;
  }

  .step-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
    padding-bottom: 16px;
    border-bottom: 2px solid var(--gray-100);
  }

  .step-label {
    font-size: 13px;
    font-weight: 700;
    color: var(--gray-600);
    text-transform: uppercase;
    letter-spacing: 1.2px;
  }

  .xp-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
    color: white;
    padding: 6px 14px;
    border-radius: var(--radius-full);
    font-size: 14px;
    font-weight: 800;
    box-shadow: 0 2px 8px rgba(251, 191, 36, 0.25);
  }

  .xp-icon {
    font-size: 16px;
  }

  .task-content {
    margin-bottom: 32px;
  }

  .task-title {
    font-size: 32px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 24px;
    line-height: 1.2;
  }

  .task-description {
    font-size: 16px;
    color: var(--gray-700);
    line-height: 1.75;
  }

  .hint-section {
    margin-top: 24px;
  }

  .btn-hint {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: "Nunito", sans-serif;
    font-size: 15px;
    font-weight: 700;
    padding: 10px 20px;
    background: white;
    color: var(--gray-700);
    border: 2px solid var(--gray-300);
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .btn-hint:hover:not(:disabled) {
    background: var(--gray-50);
    border-color: var(--gray-400);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .btn-hint:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .hint-icon {
    font-size: 18px;
  }

  .hint-cost {
    color: var(--gray-500);
    font-size: 13px;
  }

  /* RIGHT PANEL - Code Editor */
  .right-panel {
    background: #1a1d23;
    overflow-y: auto;
    height: calc(100vh - 80px);
  }

  .editor-scroll {
    padding: 32px;
  }

  /* CODE EDITOR STYLES */
  .code-section-duo {
    background: #262933;
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    margin-bottom: 24px;
  }

  .code-header {
    background: #1e2129;
    padding: 12px 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 1px solid #1a1d23;
  }

  .code-icon {
    font-size: 16px;
  }

  .code-label {
    font-size: 14px;
    font-weight: 600;
    color: #9ca3af;
    letter-spacing: 0.3px;
  }

  .code-textarea-duo {
    width: 100%;
    padding: 24px;
    font-family: "Monaco", "Menlo", "Ubuntu Mono", "Consolas", monospace;
    font-size: 14px;
    line-height: 1.7;
    background: #262933;
    color: #e5e7eb;
    border: none;
    resize: vertical;
    min-height: 400px;
    max-height: 600px;
  }

  .code-textarea-duo::placeholder {
    color: #6b7280;
  }

  .code-textarea-duo:focus {
    outline: none;
  }

  /* LOADING */
  .loading-lesson {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }

  .loading-spinner {
    font-size: 64px;
    animation: spin 1s linear infinite;
  }

  .loading-lesson p {
    margin-top: 24px;
    font-size: 20px;
    font-weight: 700;
    color: var(--gray-700);
  }

  /* ERROR MESSAGE */
  .error-message-duo {
    text-align: center;
    padding: 80px 20px;
  }

  .error-icon {
    font-size: 80px;
    margin-bottom: 24px;
  }

  .error-message-duo h3 {
    font-size: 32px;
    font-weight: 800;
    color: var(--gray-900);
    margin-bottom: 24px;
  }

  /* TOP BAR (LIKE DUOLINGO LESSON) */
  .lesson-topbar {
    background: white;
    border-bottom: 2px solid var(--gray-300);
    padding: 16px 24px;
    display: flex;
    align-items: center;
    gap: 16px;
    position: sticky;
    top: 0;
    z-index: 100;
  }

  .btn-exit {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: white;
    border: 2px solid var(--gray-400);
    color: var(--gray-700);
    font-size: 24px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    flex-shrink: 0;
  }

  .btn-exit:hover {
    background: var(--gray-100);
    border-color: var(--gray-600);
  }

  .progress-container {
    flex: 1;
    max-width: 600px;
  }

  .progress-bar-lesson {
    height: 16px;
    background: var(--gray-300);
    border-radius: var(--radius-full);
    overflow: hidden;
    position: relative;
  }

  .progress-fill-lesson {
    height: 100%;
    background: linear-gradient(90deg, var(--primary) 0%, #ff6b6b 100%);
    border-radius: var(--radius-full);
    transition: width 0.4s ease;
    box-shadow: inset 0 2px 4px rgba(255, 255, 255, 0.3);
  }

  .topbar-info {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .company-badge {
    background: var(--primary-light);
    color: var(--primary);
    padding: 8px 16px;
    border-radius: var(--radius-full);
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* RESULT FEEDBACK */
  .result-feedback-duo {
    margin-top: 20px;
    padding: 24px;
    border-radius: var(--radius-lg);
    border: 2px solid;
    animation: fadeIn 0.3s ease;
  }

  .result-feedback-duo.success {
    border-color: #22c55e;
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  }

  .result-feedback-duo.error {
    border-color: #ef4444;
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
  }

  .result-header-duo {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 20px;
  }

  .result-icon {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    font-weight: 900;
    flex-shrink: 0;
  }

  .success-icon {
    background: #22c55e;
    color: white;
    animation: checkmark 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  }

  .error-icon {
    background: #ef4444;
    color: white;
  }

  .result-text h3 {
    font-size: 20px;
    font-weight: 800;
    color: #1f2937;
    margin-bottom: 4px;
  }

  .result-text p {
    font-size: 15px;
    color: #6b7280;
    font-weight: 600;
    margin: 0;
  }

  .tests-summary {
    margin-bottom: 20px;
  }

  .test-score {
    display: inline-block;
    background: white;
    padding: 10px 20px;
    border-radius: var(--radius-md);
    font-size: 16px;
    font-weight: 800;
    color: var(--gray-900);
    border: 2px solid var(--gray-300);
  }

  /* TEST LIST */
  .test-list-duo {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .test-row-duo {
    background: white;
    padding: 16px;
    border-radius: var(--radius-md);
    border-left: 4px solid;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .test-row-duo.passed {
    border-color: var(--primary);
  }

  .test-row-duo:not(.passed) {
    border-color: #e63946;
  }

  .test-check {
    font-size: 20px;
    font-weight: 800;
    margin-right: 8px;
  }

  .test-name {
    font-size: 16px;
    font-weight: 700;
    color: var(--gray-900);
  }

  .test-details {
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-top: 8px;
    font-size: 14px;
    color: var(--gray-700);
    padding-left: 28px;
  }

  .error-code {
    margin-top: 16px;
    background: #1e1e1e;
    color: #d4d4d4;
    padding: 16px;
    border-radius: var(--radius-md);
    font-family: monospace;
    font-size: 13px;
    overflow-x: auto;
  }

  .error-code pre {
    margin: 0;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  /* BOTTOM BAR WITH CHECK BUTTON (DUOLINGO STYLE) */
  .lesson-bottombar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: white;
    border-top: 2px solid var(--gray-300);
    padding: 20px 24px;
    box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.05);
    z-index: 100;
  }

  .bottombar-content {
    max-width: 100%;
    width: 100%;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 40px;
  }

  .btn-lesson-duo {
    font-family: "Nunito", sans-serif;
    font-size: 17px;
    font-weight: 800;
    padding: 16px 40px;
    border: none;
    border-radius: var(--radius-md);
    cursor: pointer;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    transition: all 0.15s ease;
    min-width: 200px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .btn-check {
    background: linear-gradient(180deg, #58cc02 0%, #4caf00 100%);
    color: white;
    border-bottom: 4px solid #3d9400;
  }

  .btn-check:hover:not(:disabled) {
    background: linear-gradient(180deg, #61d802 0%, #56c900 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(88, 204, 2, 0.3);
  }

  .btn-check:active:not(:disabled) {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .btn-check:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .btn-continue {
    background: linear-gradient(180deg, #58cc02 0%, #4caf00 100%);
    color: white;
    border-bottom: 4px solid #3d9400;
  }

  .btn-continue:hover:not(:disabled) {
    background: linear-gradient(180deg, #61d802 0%, #56c900 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(88, 204, 2, 0.3);
  }

  .btn-continue:active:not(:disabled) {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  /* CELEBRATION OVERLAY */
  .celebration-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255, 75, 75, 0.95);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    animation: fadeIn 0.3s;
  }

  .celebration-content {
    text-align: center;
    animation: bounceIn 0.6s;
  }

  .celebration-icon {
    font-size: 120px;
    margin-bottom: 24px;
    animation: pulse 1s ease-in-out infinite;
  }

  .celebration-content h2 {
    font-size: 48px;
    font-weight: 900;
    color: white;
    margin-bottom: 16px;
  }

  .celebration-content p {
    font-size: 24px;
    font-weight: 700;
    color: white;
    opacity: 0.95;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @keyframes bounceIn {
    0% {
      transform: scale(0.3);
      opacity: 0;
    }
    50% {
      transform: scale(1.1);
    }
    100% {
      transform: scale(1);
      opacity: 1;
    }
  }

  /* EMPTY STATE */
  .empty-lesson {
    text-align: center;
    padding: 80px 20px;
  }

  .empty-icon {
    font-size: 80px;
    margin-bottom: 24px;
  }

  .empty-lesson h3 {
    font-size: 28px;
    font-weight: 800;
    color: var(--gray-900);
    margin-bottom: 12px;
  }

  .empty-lesson p {
    font-size: 18px;
    color: var(--gray-700);
    margin-bottom: 32px;
  }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .lesson-topbar {
      padding: 12px 16px;
    }

    .company-badge {
      display: none;
    }

    .lesson-container {
      padding: 24px 16px 100px;
    }

    .task-card-duo {
      padding: 24px;
    }

    .task-title {
      font-size: 24px;
    }

    .task-description {
      font-size: 16px;
    }

    .code-textarea-duo {
      font-size: 13px;
      padding: 16px;
    }

    .btn-lesson-duo {
      width: 100%;
      min-width: auto;
    }

    .celebration-icon {
      font-size: 80px;
    }

    .celebration-content h2 {
      font-size: 36px;
    }

    .celebration-content p {
      font-size: 18px;
    }
  }
</style>
