# ── Prospera SYSTEM HEADER (ADR-0032/SBOM) ──
# 性質:data ｜設計:Kevin 架構 ｜執行:AI 工具(claude.ai+Claude Code)
# 驗證:無機制驗證 ｜IP:創造性歸 Kevin(發明人), AI 為執行工具 (ADR-0032)
param ([string]$SupplierGID = "SUP-TW-TP-001")
$ReportPath = "Registry\VALUATION\GLOBAL_SUPPLY_CHAIN_REPORT.md"
if (!(Test-Path $ReportPath)) { Write-Error "Report missing"; return }
$Report = Get-Content $ReportPath
$Intensity = ($Report | Select-String "Average Carbon Intensity: (\d+\.?\d*)").Matches.Groups[1].Value
$Rank = "B"; if ([double]$Intensity -lt 10.0) { $Rank = "AAA" }
$CreditData = @{ supplier_gid = $SupplierGID; credit_rank = $Rank; date = (Get-Date).ToString("yyyy-MM-dd") } | ConvertTo-Json
if (!(Test-Path "Registry\KEYS")) { New-Item "Registry\KEYS" -ItemType Directory -Force }
$CreditData | Set-Content -Path "Registry\KEYS\SUPPLIER_CREDITS.json" -Encoding UTF8
Write-Host ">>> Credit Issued: $Rank for $SupplierGID" -ForegroundColor Green
