<script>
  import { onMount } from "svelte";

  let user = {
    name: "Diego Alonso Rojas Vera",
    email: "diego.rojas@example.com",
  };

  let certificates = [
    {
      id: 1,
      courseName: "Data Science para Fintech",
      courseCode: "DS-FIN-001",
      completionDate: "15 de Octubre, 2025",
      instructor: "Dr. Carlos Mendoza",
      hours: 180,
      grade: 95,
      skills: [
        "Python",
        "Machine Learning",
        "Análisis Financiero",
        "SQL",
        "Pandas",
        "Scikit-learn",
      ],
      issueDate: "2025-10-15",
      certificateNumber: "WIN-DSFIN-001-2025-1547",
      sponsorCompany: "PagoSeguro",
      sponsorLogo: "/src/logos_empresas/Pagoseguro.png",
      sponsorRole: "Empresa Patrocinadora",
    },
    {
      id: 3,
      courseName: "Big Data y Analytics",
      courseCode: "DS-BDA-003",
      completionDate: "10 de Agosto, 2025",
      instructor: "Ing. Roberto Silva",
      hours: 160,
      grade: 89,
      skills: [
        "Hadoop",
        "Spark",
        "Tableau",
        "Power BI",
        "Data Warehousing",
        "ETL",
      ],
      issueDate: "2025-08-10",
      certificateNumber: "WIN-DSBDA-003-2025-0892",
      sponsorCompany: "AgroData",
      sponsorLogo: "/src/logos_empresas/Agrodata.png",
      sponsorRole: "Empresa Patrocinadora",
    },
  ];

  let selectedCertificate = certificates[0];
  let showPreview = false;

  function previewCertificate(cert) {
    selectedCertificate = cert;
    showPreview = true;
  }

  function closePreview() {
    showPreview = false;
  }
</script>

<svelte:head>
  <title>Mis Certificados - Wiñay</title>
</svelte:head>

<div class="certificates-page">
  <!-- HEADER -->
  <div class="header-certificates">
    <div class="container">
      <h1>📜 Mis Certificados</h1>
      <p class="subtitle">
        Descarga y comparte tus logros académicos con el mundo
      </p>

      <!-- Stats -->
      <div class="stats-bar-certs">
        <div class="stat-card-cert">
          <div class="stat-icon-cert">🎓</div>
          <div>
            <div class="stat-value-cert">{certificates.length}</div>
            <div class="stat-label-cert">Certificados</div>
          </div>
        </div>
        <div class="stat-card-cert">
          <div class="stat-icon-cert">⏱️</div>
          <div>
            <div class="stat-value-cert">
              {certificates.reduce((sum, c) => sum + c.hours, 0)}h
            </div>
            <div class="stat-label-cert">Horas Totales</div>
          </div>
        </div>
        <div class="stat-card-cert">
          <div class="stat-icon-cert">⭐</div>
          <div>
            <div class="stat-value-cert">
              {Math.round(
                certificates.reduce((sum, c) => sum + c.grade, 0) /
                  certificates.length
              )}%
            </div>
            <div class="stat-label-cert">Promedio</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- CERTIFICATES LIST -->
  <div class="container">
    <div class="certificates-grid">
      {#each certificates as certificate}
        <div class="certificate-card">
          <div class="certificate-card-header">
            <div class="cert-icon">🎓</div>
            <div class="cert-badge">Completado</div>
          </div>

          <div class="certificate-card-body">
            <h3 class="cert-title">{certificate.courseName}</h3>
            <div class="cert-code">{certificate.courseCode}</div>

            <div class="cert-meta">
              <div class="meta-item">
                <span class="meta-icon">📅</span>
                <span class="meta-text">{certificate.completionDate}</span>
              </div>
              <div class="meta-item">
                <span class="meta-icon">👨‍🏫</span>
                <span class="meta-text">{certificate.instructor}</span>
              </div>
              <div class="meta-item">
                <span class="meta-icon">⏱️</span>
                <span class="meta-text">{certificate.hours} horas</span>
              </div>
              <div class="meta-item">
                <span class="meta-icon">📊</span>
                <span class="meta-text">Calificación: {certificate.grade}%</span
                >
              </div>
            </div>

            <div class="cert-skills">
              <div class="skills-label">Habilidades:</div>
              <div class="skills-tags">
                {#each certificate.skills as skill}
                  <span class="skill-tag">{skill}</span>
                {/each}
              </div>
            </div>

            <div class="cert-actions">
              <button
                class="btn-preview"
                on:click={() => previewCertificate(certificate)}
              >
                <span>👁️</span>
                <span>Previsualizar</span>
              </button>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>

<!-- MODAL PREVIEW -->
{#if showPreview}
  <div class="modal-overlay" on:click={closePreview}>
    <div class="modal-content" on:click|stopPropagation>
      <button class="btn-close" on:click={closePreview}>✕</button>

      <!-- CERTIFICATE DESIGN -->
      <div class="certificate-preview">
        <!-- Border -->
        <div class="cert-border">
          <div class="cert-inner-border">
            <!-- Header -->
            <div class="cert-header-section">
              <div class="cert-logo">🎓</div>
              <h2 class="cert-platform">WIÑAY</h2>
              <p class="cert-platform-subtitle">
                Plataforma de Educación Superior
              </p>
            </div>

            <!-- Title -->
            <div class="cert-title-section">
              <h1 class="cert-main-title">CERTIFICADO DE FINALIZACIÓN</h1>
              <div class="cert-divider"></div>
            </div>

            <!-- Body -->
            <div class="cert-body-section">
              <p class="cert-text">Este certificado se otorga a</p>
              <h2 class="cert-student-name">{user.name}</h2>
              <p class="cert-text">
                por haber completado exitosamente el curso
              </p>
              <h3 class="cert-course-name">{selectedCertificate.courseName}</h3>
              <p class="cert-course-code">
                Código: {selectedCertificate.courseCode}
              </p>
            </div>

            <!-- Details -->
            <div class="cert-details-section">
              <div class="cert-detail-item">
                <div class="detail-label">Fecha de Finalización</div>
                <div class="detail-value">
                  {selectedCertificate.completionDate}
                </div>
              </div>
              <div class="cert-detail-item">
                <div class="detail-label">Duración del Curso</div>
                <div class="detail-value">
                  {selectedCertificate.hours} horas académicas
                </div>
              </div>
              <div class="cert-detail-item">
                <div class="detail-label">Calificación Final</div>
                <div class="detail-value">{selectedCertificate.grade}%</div>
              </div>
            </div>

            <!-- Sponsor Company Section -->
            {#if selectedCertificate.sponsorCompany}
              <div class="cert-sponsor-section">
                <div class="sponsor-label">EN COLABORACIÓN CON</div>
                <div class="sponsor-box">
                  <img
                    src={selectedCertificate.sponsorLogo}
                    alt={selectedCertificate.sponsorCompany}
                    class="sponsor-logo-large"
                  />
                  <div class="sponsor-info">
                    <div class="sponsor-company-name">
                      {selectedCertificate.sponsorCompany}
                    </div>
                    <div class="sponsor-role">
                      {selectedCertificate.sponsorRole}
                    </div>
                  </div>
                </div>
                <p class="sponsor-text">
                  Este programa ha sido desarrollado en colaboración con {selectedCertificate.sponsorCompany},
                  garantizando contenido alineado con las necesidades reales de
                  la industria.
                </p>
              </div>
            {/if}

            <!-- Footer -->
            <div class="cert-footer-section">
              <div class="cert-signature">
                <div class="signature-line"></div>
                <div class="signature-name">
                  {selectedCertificate.instructor}
                </div>
                <div class="signature-title">Instructor del Curso</div>
              </div>
              <div class="cert-seal">
                <div class="seal-circle">
                  <div class="seal-text">WIÑAY</div>
                  <div class="seal-year">2025</div>
                </div>
              </div>
              <div class="cert-signature">
                <div class="signature-line"></div>
                <div class="signature-name">Dr. Juan Pérez</div>
                <div class="signature-title">Director Académico</div>
              </div>
            </div>

            <!-- Certificate Number -->
            <div class="cert-number-section">
              <p class="cert-number">
                Certificado N° {selectedCertificate.certificateNumber}
              </p>
              <p class="cert-verification">
                Verificar autenticidad en: www.winay.edu.pe/verify
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  .certificates-page {
    min-height: calc(100vh - 80px);
    background: var(--bg);
    padding-bottom: 80px;
  }

  /* HEADER */
  .header-certificates {
    padding: 48px 0 40px;
    text-align: center;
    background: linear-gradient(135deg, #fef3c7 0%, #ffffff 100%);
    border-bottom: 2px solid var(--gray-200);
  }

  .header-certificates h1 {
    font-size: 42px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 12px;
    letter-spacing: -0.5px;
  }

  .subtitle {
    font-size: 18px;
    color: var(--gray-600);
    margin-bottom: 32px;
  }

  .stats-bar-certs {
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .stat-card-cert {
    background: white;
    border-radius: var(--radius-lg);
    padding: 20px 28px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    border: 2px solid #fbbf24;
  }

  .stat-icon-cert {
    font-size: 36px;
  }

  .stat-value-cert {
    font-size: 28px;
    font-weight: 900;
    color: #f59e0b;
    line-height: 1;
  }

  .stat-label-cert {
    font-size: 13px;
    font-weight: 600;
    color: var(--gray-600);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* CERTIFICATES GRID */
  .certificates-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
    gap: 24px;
    padding: 40px 0;
  }

  .certificate-card {
    background: white;
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s;
    border: 2px solid var(--gray-200);
  }

  .certificate-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
    border-color: #f59e0b;
  }

  .certificate-card-header {
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
    padding: 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .cert-icon {
    font-size: 48px;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
  }

  .cert-badge {
    background: white;
    color: #f59e0b;
    padding: 6px 14px;
    border-radius: var(--radius-full);
    font-size: 12px;
    font-weight: 800;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .certificate-card-body {
    padding: 24px;
  }

  .cert-title {
    font-size: 20px;
    font-weight: 900;
    color: var(--gray-900);
    margin-bottom: 8px;
    line-height: 1.3;
  }

  .cert-code {
    font-size: 13px;
    font-weight: 700;
    color: var(--gray-500);
    margin-bottom: 20px;
  }

  .cert-meta {
    background: var(--bg-gray);
    border-radius: var(--radius-md);
    padding: 16px;
    margin-bottom: 20px;
  }

  .meta-item {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }

  .meta-item:last-child {
    margin-bottom: 0;
  }

  .meta-icon {
    font-size: 16px;
  }

  .meta-text {
    font-size: 14px;
    font-weight: 600;
    color: var(--gray-700);
  }

  .cert-skills {
    margin-bottom: 24px;
  }

  .skills-label {
    font-size: 13px;
    font-weight: 700;
    color: var(--gray-600);
    margin-bottom: 10px;
  }

  .skills-tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }

  .skill-tag {
    background: #fef3c7;
    color: #92400e;
    padding: 4px 12px;
    border-radius: var(--radius-full);
    font-size: 12px;
    font-weight: 700;
  }

  .cert-actions {
    display: flex;
    gap: 12px;
  }

  .btn-preview {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 12px 16px;
    border-radius: var(--radius-md);
    font-size: 14px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    border: none;
    background: var(--primary);
    color: white;
  }

  .btn-preview:hover {
    background: var(--primary-hover);
    transform: scale(1.02);
  }

  /* MODAL */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    padding: 20px;
    overflow-y: auto;
  }

  .modal-content {
    background: white;
    border-radius: var(--radius-lg);
    padding: 40px;
    max-width: 900px;
    width: 100%;
    position: relative;
    max-height: 90vh;
    overflow-y: auto;
  }

  .btn-close {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--gray-200);
    border: none;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.2s;
    z-index: 10;
  }

  .btn-close:hover {
    background: var(--primary);
    color: white;
  }

  /* CERTIFICATE DESIGN */
  .certificate-preview {
    margin-bottom: 30px;
  }

  .cert-border {
    padding: 20px;
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 50%, #dc2626 100%);
    border-radius: 12px;
  }

  .cert-inner-border {
    background: white;
    padding: 50px 60px;
    border-radius: 8px;
    border: 3px solid #f59e0b;
  }

  .cert-header-section {
    text-align: center;
    margin-bottom: 30px;
  }

  .cert-logo {
    font-size: 64px;
    margin-bottom: 10px;
  }

  .cert-platform {
    font-size: 36px;
    font-weight: 900;
    color: var(--primary);
    letter-spacing: 4px;
    margin-bottom: 5px;
  }

  .cert-platform-subtitle {
    font-size: 14px;
    color: var(--gray-600);
    font-weight: 600;
  }

  .cert-title-section {
    text-align: center;
    margin-bottom: 40px;
  }

  .cert-main-title {
    font-size: 28px;
    font-weight: 900;
    color: var(--gray-900);
    letter-spacing: 2px;
    margin-bottom: 15px;
  }

  .cert-divider {
    width: 200px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #f59e0b, transparent);
    margin: 0 auto;
  }

  .cert-body-section {
    text-align: center;
    margin-bottom: 40px;
  }

  .cert-text {
    font-size: 16px;
    color: var(--gray-600);
    margin-bottom: 10px;
    font-style: italic;
  }

  .cert-student-name {
    font-size: 42px;
    font-weight: 900;
    color: var(--primary);
    margin: 20px 0;
    font-family: "Georgia", serif;
    letter-spacing: 1px;
  }

  .cert-course-name {
    font-size: 28px;
    font-weight: 800;
    color: var(--gray-900);
    margin: 20px 0;
  }

  .cert-course-code {
    font-size: 14px;
    color: var(--gray-500);
    font-weight: 600;
  }

  .cert-details-section {
    display: flex;
    justify-content: space-around;
    margin-bottom: 30px;
    padding: 20px 0;
    border-top: 2px solid var(--gray-200);
    border-bottom: 2px solid var(--gray-200);
  }

  /* SPONSOR SECTION */
  .cert-sponsor-section {
    text-align: center;
    margin-bottom: 40px;
    padding: 30px;
    background: linear-gradient(135deg, #fef3c7 0%, white 100%);
    border-radius: 8px;
    border: 2px dashed #f59e0b;
  }

  .sponsor-label {
    font-size: 11px;
    font-weight: 800;
    color: #92400e;
    letter-spacing: 2px;
    margin-bottom: 15px;
  }

  .sponsor-box {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin-bottom: 15px;
  }

  .sponsor-logo-large {
    width: 100px;
    height: 100px;
    object-fit: contain;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
    background: white;
    border-radius: 8px;
    padding: 8px;
  }

  .sponsor-info {
    text-align: left;
  }

  .sponsor-company-name {
    font-size: 24px;
    font-weight: 900;
    color: var(--gray-900);
    line-height: 1.2;
  }

  .sponsor-role {
    font-size: 12px;
    font-weight: 700;
    color: #f59e0b;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  .sponsor-text {
    font-size: 12px;
    color: var(--gray-600);
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto;
    font-style: italic;
  }

  .cert-detail-item {
    text-align: center;
  }

  .detail-label {
    font-size: 12px;
    font-weight: 700;
    color: var(--gray-500);
    text-transform: uppercase;
    margin-bottom: 8px;
  }

  .detail-value {
    font-size: 16px;
    font-weight: 800;
    color: var(--gray-900);
  }

  .cert-footer-section {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 30px;
  }

  .cert-signature {
    text-align: center;
  }

  .signature-line {
    width: 180px;
    height: 2px;
    background: var(--gray-400);
    margin-bottom: 8px;
  }

  .signature-name {
    font-size: 14px;
    font-weight: 800;
    color: var(--gray-900);
    margin-bottom: 4px;
  }

  .signature-title {
    font-size: 11px;
    color: var(--gray-600);
    font-weight: 600;
  }

  .cert-seal {
    text-align: center;
  }

  .seal-circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 4px solid #f59e0b;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #fef3c7 0%, white 100%);
  }

  .seal-text {
    font-size: 16px;
    font-weight: 900;
    color: #f59e0b;
  }

  .seal-year {
    font-size: 12px;
    font-weight: 700;
    color: var(--gray-600);
  }

  .cert-number-section {
    text-align: center;
  }

  .cert-number {
    font-size: 11px;
    font-weight: 700;
    color: var(--gray-500);
    margin-bottom: 4px;
  }

  .cert-verification {
    font-size: 10px;
    color: var(--gray-400);
    font-weight: 600;
  }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .certificates-grid {
      grid-template-columns: 1fr;
    }

    .cert-inner-border {
      padding: 30px 20px;
    }

    .cert-student-name {
      font-size: 28px;
    }

    .cert-course-name {
      font-size: 20px;
    }

    .cert-details-section {
      flex-direction: column;
      gap: 16px;
    }

    .cert-footer-section {
      flex-direction: column;
      gap: 20px;
      align-items: center;
    }

    .sponsor-box {
      flex-direction: column;
      gap: 10px;
    }

    .sponsor-info {
      text-align: center;
    }

    .sponsor-company-name {
      font-size: 20px;
    }

    .modal-content {
      padding: 20px;
    }
  }
</style>
