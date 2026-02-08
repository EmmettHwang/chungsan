// API 기본 URL
const API_BASE_URL = 'http://localhost:8001/api';

// 전역 변수
let currentParticipantId = null;
let currentProjectId = null;
let allParticipants = []; // 모든 참여자 목록
let projectParticipants = []; // 프로젝트 참여자 목록 (수익률 포함)

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', function() {
    // 대시보드 데이터 로드
    loadDashboard();
    
    // 역할 선택 시 기본 수익률 자동 설정
    const roleSelect = document.getElementById('participant-role');
    if (roleSelect) {
        roleSelect.addEventListener('change', function() {
            setDefaultProfitRate(this.value);
        });
    }
});

// 페이지 전환
function showPage(pageName) {
    // 모든 페이지 숨기기
    document.querySelectorAll('.page-content').forEach(page => {
        page.style.display = 'none';
    });
    
    // 선택된 페이지 표시
    document.getElementById(pageName + '-page').style.display = 'block';
    
    // 네비게이션 활성화
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });
    event.target.classList.add('active');
    
    // 페이지별 데이터 로드
    switch(pageName) {
        case 'dashboard':
            loadDashboard();
            break;
        case 'participants':
            loadParticipants();
            break;
        case 'projects':
            loadProjects();
            break;
        case 'settlements':
            loadSettlementsPage();
            break;
    }
}

// 대시보드 데이터 로드
async function loadDashboard() {
    try {
        // 참여자 통계
        const participants = await fetchAPI('/participants/');
        document.getElementById('total-participants').textContent = participants.length;
        
        // 프로젝트 통계
        const projects = await fetchAPI('/projects/');
        const activeProjects = projects.filter(p => p.status === 'in_progress').length;
        const completedProjects = projects.filter(p => p.status === 'completed').length;
        
        document.getElementById('active-projects').textContent = activeProjects;
        document.getElementById('completed-projects').textContent = completedProjects;
        
        // 총 정산액 계산 (완료된 프로젝트의 순이익 합계)
        const totalSettlements = projects
            .filter(p => p.status === 'completed')
            .reduce((sum, p) => sum + (p.profit || 0), 0);
        document.getElementById('total-settlements').textContent = formatCurrency(totalSettlements);
        
        // 최근 프로젝트 표시
        displayRecentProjects(projects.slice(0, 5));
        
    } catch (error) {
        console.error('대시보드 로드 실패:', error);
        showAlert('대시보드를 불러오는데 실패했습니다.', 'danger');
    }
}

// 최근 프로젝트 표시
function displayRecentProjects(projects) {
    const tbody = document.getElementById('recent-projects-table');
    
    if (projects.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="6" class="text-center text-muted">프로젝트가 없습니다.</td>
            </tr>
        `;
        return;
    }
    
    tbody.innerHTML = projects.map(project => `
        <tr>
            <td><strong>${project.name}</strong></td>
            <td>${project.client}</td>
            <td>${formatCurrency(project.total_amount)}</td>
            <td class="amount">${formatCurrency(project.profit)}</td>
            <td>${getStatusBadge(project.status)}</td>
            <td>
                <button class="btn btn-sm btn-primary" onclick="viewProjectDetails(${project.id})">
                    <i class="fas fa-eye"></i>
                </button>
            </td>
        </tr>
    `).join('');
}

// 참여자 목록 로드
async function loadParticipants() {
    try {
        const participants = await fetchAPI('/participants/');
        const tbody = document.getElementById('participants-table');
        
        if (participants.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="8" class="text-center text-muted">참여자가 없습니다.</td>
                </tr>
            `;
            return;
        }
        
        tbody.innerHTML = participants.map(p => `
            <tr>
                <td><span class="badge bg-secondary">${p.code}</span></td>
                <td><strong>${p.name}</strong></td>
                <td>${getRoleBadge(p.role)}</td>
                <td><span class="badge bg-info">${p.default_profit_rate}%</span></td>
                <td>${p.phone || '-'}</td>
                <td>${p.bank_name || '-'}</td>
                <td>${p.account_number || '-'}</td>
                <td>
                    <div class="action-buttons">
                        <button class="btn btn-sm btn-warning" onclick="editParticipant(${p.id})">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" onclick="deleteParticipant(${p.id}, '${p.name}')">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </td>
            </tr>
        `).join('');
        
    } catch (error) {
        console.error('참여자 로드 실패:', error);
        showAlert('참여자 목록을 불러오는데 실패했습니다.', 'danger');
    }
}

// 프로젝트 목록 로드
async function loadProjects() {
    try {
        const projects = await fetchAPI('/projects/');
        const tbody = document.getElementById('projects-table');
        
        if (projects.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="7" class="text-center text-muted">프로젝트가 없습니다.</td>
                </tr>
            `;
            return;
        }
        
        tbody.innerHTML = projects.map(p => `
            <tr>
                <td><strong>${p.name}</strong></td>
                <td>${p.client}</td>
                <td>${formatCurrency(p.total_amount)}</td>
                <td>${formatCurrency(p.cost)}</td>
                <td class="amount">${formatCurrency(p.profit)}</td>
                <td>${getStatusBadge(p.status)}</td>
                <td>
                    <div class="action-buttons">
                        <button class="btn btn-sm btn-info" onclick="viewProjectDetails(${p.id})">
                            <i class="fas fa-eye"></i>
                        </button>
                        <button class="btn btn-sm btn-warning" onclick="editProject(${p.id})">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" onclick="deleteProject(${p.id}, '${p.name}')">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </td>
            </tr>
        `).join('');
        
    } catch (error) {
        console.error('프로젝트 로드 실패:', error);
        showAlert('프로젝트 목록을 불러오는데 실패했습니다.', 'danger');
    }
}

// 정산 페이지 로드
async function loadSettlementsPage() {
    try {
        const projects = await fetchAPI('/projects/');
        const select = document.getElementById('settlement-project-select');
        
        select.innerHTML = '<option value="">프로젝트를 선택하세요</option>';
        projects.forEach(p => {
            select.innerHTML += `<option value="${p.id}">${p.name} (${p.client})</option>`;
        });
        
        // 결과 초기화
        document.getElementById('settlement-result').innerHTML = `
            <p class="text-center text-muted">
                프로젝트를 선택하고 정산 계산 버튼을 클릭하세요.
            </p>
        `;
        
    } catch (error) {
        console.error('정산 페이지 로드 실패:', error);
        showAlert('정산 페이지를 불러오는데 실패했습니다.', 'danger');
    }
}

// 정산 계산
async function calculateSettlement() {
    const projectId = document.getElementById('settlement-project-select').value;
    
    if (!projectId) {
        showAlert('프로젝트를 선택해주세요.', 'warning');
        return;
    }
    
    try {
        const result = await fetchAPI('/settlements/calculate', {
            method: 'POST',
            body: JSON.stringify({ project_id: parseInt(projectId) })
        });
        
        displaySettlementResult(result);
        showAlert('정산이 계산되었습니다!', 'success');
        
    } catch (error) {
        console.error('정산 계산 실패:', error);
        showAlert('정산 계산에 실패했습니다: ' + error.message, 'danger');
    }
}

// 정산 결과 표시
function displaySettlementResult(result) {
    const container = document.getElementById('settlement-result');
    
    container.innerHTML = `
        <div class="settlement-card">
            <h3><i class="fas fa-chart-pie"></i> ${result.project_name}</h3>
            <div class="settlement-info">
                <div>
                    <strong>총 순이익</strong><br>
                    <span style="font-size: 1.5rem;">${formatCurrency(result.total_profit)}</span>
                </div>
                <div class="text-end">
                    <strong>참여자 수</strong><br>
                    <span style="font-size: 1.5rem;">${result.settlements.length}명</span>
                </div>
            </div>
        </div>
        
        <div class="mt-3">
            <h5 class="mb-3"><i class="fas fa-users"></i> 참여자별 정산 내역</h5>
            ${result.settlements.map(s => `
                <div class="participant-settlement">
                    <div class="participant-info">
                        <div>
                            <span class="participant-name">${s.participant_name}</span>
                            <span class="participant-code">${s.participant_code}</span>
                        </div>
                        ${getRoleBadge(s.participant_role || 'regular')}
                    </div>
                    <div class="profit-info">
                        <span class="profit-rate">${s.profit_rate}%</span>
                        <span class="profit-amount">${formatCurrency(s.amount)}</span>
                    </div>
                </div>
            `).join('')}
        </div>
        
        <div class="mt-3 text-center">
            <button class="btn btn-success" onclick="printSettlement()">
                <i class="fas fa-print"></i> 인쇄하기
            </button>
            <button class="btn btn-primary" onclick="exportSettlement()">
                <i class="fas fa-download"></i> 엑셀 다운로드
            </button>
        </div>
    `;
}

// 참여자 모달 표시
function showParticipantModal(participantId = null) {
    currentParticipantId = participantId;
    const modal = new bootstrap.Modal(document.getElementById('participantModal'));
    
    if (participantId) {
        document.getElementById('participant-modal-title').textContent = '참여자 수정';
        loadParticipantData(participantId);
    } else {
        document.getElementById('participant-modal-title').textContent = '참여자 추가';
        document.getElementById('participant-form').reset();
        document.getElementById('participant-id').value = '';
    }
    
    modal.show();
}

// 참여자 데이터 로드
async function loadParticipantData(id) {
    try {
        const participant = await fetchAPI(`/participants/${id}`);
        
        document.getElementById('participant-id').value = participant.id;
        document.getElementById('participant-name').value = participant.name;
        document.getElementById('participant-role').value = participant.role;
        document.getElementById('participant-profit-rate').value = participant.default_profit_rate;
        document.getElementById('participant-phone').value = participant.phone || '';
        document.getElementById('participant-bank').value = participant.bank_name || '';
        document.getElementById('participant-account').value = participant.account_number || '';
        document.getElementById('participant-email').value = participant.email || '';
        document.getElementById('participant-notes').value = participant.notes || '';
        
    } catch (error) {
        console.error('참여자 데이터 로드 실패:', error);
        showAlert('참여자 정보를 불러오는데 실패했습니다.', 'danger');
    }
}

// 참여자 저장
async function saveParticipant() {
    const id = document.getElementById('participant-id').value;
    const data = {
        name: document.getElementById('participant-name').value,
        role: document.getElementById('participant-role').value,
        default_profit_rate: parseFloat(document.getElementById('participant-profit-rate').value),
        phone: document.getElementById('participant-phone').value || null,
        bank_name: document.getElementById('participant-bank').value || null,
        account_number: document.getElementById('participant-account').value || null,
        email: document.getElementById('participant-email').value || null,
        notes: document.getElementById('participant-notes').value || null
    };
    
    try {
        if (id) {
            await fetchAPI(`/participants/${id}`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
            showAlert('참여자가 수정되었습니다!', 'success');
        } else {
            await fetchAPI('/participants/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
            showAlert('참여자가 추가되었습니다!', 'success');
        }
        
        bootstrap.Modal.getInstance(document.getElementById('participantModal')).hide();
        loadParticipants();
        loadDashboard();
        
    } catch (error) {
        console.error('참여자 저장 실패:', error);
        showAlert('참여자 저장에 실패했습니다: ' + error.message, 'danger');
    }
}

// 참여자 수정
function editParticipant(id) {
    showParticipantModal(id);
}

// 참여자 삭제
async function deleteParticipant(id, name) {
    if (!confirm(`정말로 "${name}" 참여자를 삭제하시겠습니까?`)) {
        return;
    }
    
    try {
        await fetchAPI(`/participants/${id}`, { method: 'DELETE' });
        showAlert('참여자가 삭제되었습니다.', 'success');
        loadParticipants();
        loadDashboard();
    } catch (error) {
        console.error('참여자 삭제 실패:', error);
        showAlert('참여자 삭제에 실패했습니다: ' + error.message, 'danger');
    }
}

// 프로젝트 모달 표시
async function showProjectModal(projectId = null) {
    currentProjectId = projectId;
    
    // 참여자 목록 먼저 로드
    await loadAllParticipants();
    
    const modal = new bootstrap.Modal(document.getElementById('projectModal'));
    
    if (projectId) {
        document.getElementById('project-modal-title').textContent = '프로젝트 수정';
        await loadProjectData(projectId);
    } else {
        document.getElementById('project-modal-title').textContent = '프로젝트 추가';
        document.getElementById('project-form').reset();
        document.getElementById('project-id').value = '';
        projectParticipants = [];
        
        // 아이디어 날짜를 오늘로 자동 설정
        const today = new Date().toISOString().split('T')[0];
        document.getElementById('project-idea-date').value = today;
    }
    
    // 참여자 체크박스 목록 생성
    renderParticipantsList();
    
    // 프로그레스 바 업데이트
    setTimeout(updateProgressBar, 100);
    
    modal.show();
}

// 프로젝트 데이터 로드
async function loadProjectData(id) {
    try {
        const project = await fetchAPI(`/projects/${id}`);
        
        // 기본 정보
        document.getElementById('project-id').value = project.id;
        document.getElementById('project-name').value = project.name;
        document.getElementById('project-client').value = project.client;
        document.getElementById('project-total-amount').value = project.total_amount;
        document.getElementById('project-cost').value = project.cost;
        document.getElementById('project-status').value = project.status;
        document.getElementById('project-start-date').value = project.start_date || '';
        document.getElementById('project-end-date').value = project.end_date || '';
        document.getElementById('project-notes').value = project.notes || '';
        
        // 10단계 날짜 로드
        document.getElementById('project-idea-date').value = project.idea_date || '';
        document.getElementById('project-introduction-date').value = project.introduction_date || '';
        document.getElementById('project-consultation-date').value = project.consultation_date || '';
        document.getElementById('project-quote-date').value = project.quote_date || '';
        document.getElementById('project-contract-date').value = project.contract_date || '';
        document.getElementById('project-development-date').value = project.development_date || '';
        document.getElementById('project-test-date').value = project.test_date || '';
        document.getElementById('project-delivery-date').value = project.delivery_date || '';
        document.getElementById('project-completion-date').value = project.completion_date || '';
        document.getElementById('project-maintenance-date').value = project.maintenance_date || '';
        
        // 진도 정보 로드
        document.getElementById('project-progress-notes').value = project.progress_notes || '';
        document.getElementById('project-current-stage').value = project.current_stage || '';
        document.getElementById('project-progress-rate').value = project.progress_rate || '';
        
        // 프로젝트 참여자 로드
        await loadProjectParticipants(id);
        
    } catch (error) {
        console.error('프로젝트 데이터 로드 실패:', error);
        showAlert('프로젝트 정보를 불러오는데 실패했습니다.', 'danger');
    }
}

// 프로젝트 저장
async function saveProject() {
    const id = document.getElementById('project-id').value;
    
    // 기본 정보
    const data = {
        name: document.getElementById('project-name').value,
        client: document.getElementById('project-client').value,
        total_amount: parseFloat(document.getElementById('project-total-amount').value),
        cost: parseFloat(document.getElementById('project-cost').value),
        status: document.getElementById('project-status').value,
        start_date: document.getElementById('project-start-date').value || null,
        end_date: document.getElementById('project-end-date').value || null,
        notes: document.getElementById('project-notes').value || null,
        
        // 10단계 날짜
        idea_date: document.getElementById('project-idea-date').value || null,
        introduction_date: document.getElementById('project-introduction-date').value || null,
        consultation_date: document.getElementById('project-consultation-date').value || null,
        quote_date: document.getElementById('project-quote-date').value || null,
        contract_date: document.getElementById('project-contract-date').value || null,
        development_date: document.getElementById('project-development-date').value || null,
        test_date: document.getElementById('project-test-date').value || null,
        delivery_date: document.getElementById('project-delivery-date').value || null,
        completion_date: document.getElementById('project-completion-date').value || null,
        maintenance_date: document.getElementById('project-maintenance-date').value || null,
        
        // 진도 정보
        progress_notes: document.getElementById('project-progress-notes').value || null,
        current_stage: document.getElementById('project-current-stage').value || null,
        progress_rate: document.getElementById('project-progress-rate').value ? parseFloat(document.getElementById('project-progress-rate').value) : null
    };
    
    try {
        let projectId = id;
        
        if (id) {
            // 프로젝트 수정
            await fetchAPI(`/projects/${id}`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        } else {
            // 프로젝트 생성
            const newProject = await fetchAPI('/projects/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
            projectId = newProject.id;
        }
        
        // 참여자 저장 (선택된 참여자만)
        const selectedParticipants = projectParticipants.filter(p => p.selected);
        for (const p of selectedParticipants) {
            try {
                await fetchAPI(`/projects/${projectId}/participants`, {
                    method: 'POST',
                    body: JSON.stringify({
                        participant_id: p.id,
                        profit_rate: p.profit_rate || p.default_profit_rate
                    })
                });
            } catch (err) {
                console.error(`참여자 ${p.name} 추가 실패:`, err);
            }
        }
        
        showAlert(id ? '프로젝트가 수정되었습니다!' : '프로젝트가 추가되었습니다!', 'success');
        
        bootstrap.Modal.getInstance(document.getElementById('projectModal')).hide();
        loadProjects();
        loadDashboard();
        
    } catch (error) {
        console.error('프로젝트 저장 실패:', error);
        showAlert('프로젝트 저장에 실패했습니다: ' + error.message, 'danger');
    }
}

// 프로젝트 수정
function editProject(id) {
    showProjectModal(id);
}

// 프로젝트 삭제
async function deleteProject(id, name) {
    if (!confirm(`정말로 "${name}" 프로젝트를 삭제하시겠습니까?`)) {
        return;
    }
    
    try {
        await fetchAPI(`/projects/${id}`, { method: 'DELETE' });
        showAlert('프로젝트가 삭제되었습니다.', 'success');
        loadProjects();
        loadDashboard();
    } catch (error) {
        console.error('프로젝트 삭제 실패:', error);
        showAlert('프로젝트 삭제에 실패했습니다: ' + error.message, 'danger');
    }
}

// 프로젝트 상세 보기
function viewProjectDetails(id) {
    // TODO: 프로젝트 상세 모달 구현
    alert('프로젝트 상세 보기 (구현 예정)');
}

// API 호출 헬퍼 함수
async function fetchAPI(endpoint, options = {}) {
    const url = API_BASE_URL + endpoint;
    const defaultOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    
    const finalOptions = { ...defaultOptions, ...options };
    
    const response = await fetch(url, finalOptions);
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || '요청 실패');
    }
    
    return await response.json();
}

// 역할별 기본 수익률 설정
function setDefaultProfitRate(role) {
    const rates = {
        'admin': 30,
        'lead': 25,
        'senior': 20,
        'regular': 15,
        'assistant': 10
    };
    
    document.getElementById('participant-profit-rate').value = rates[role] || 15;
}

// 역할 뱃지 생성
function getRoleBadge(role) {
    const roleNames = {
        'admin': '관리자',
        'lead': '팀장',
        'senior': '선임',
        'regular': '일반',
        'assistant': '보조'
    };
    
    return `<span class="badge role-badge role-${role}">${roleNames[role] || role}</span>`;
}

// 상태 뱃지 생성
function getStatusBadge(status) {
    const statusNames = {
        'planning': '기획 중',
        'in_progress': '진행 중',
        'completed': '완료',
        'cancelled': '취소'
    };
    
    return `<span class="badge status-badge status-${status}">${statusNames[status] || status}</span>`;
}

// 금액 포맷
function formatCurrency(amount) {
    if (!amount && amount !== 0) return '-';
    return new Intl.NumberFormat('ko-KR', {
        style: 'currency',
        currency: 'KRW'
    }).format(amount);
}

// 알림 표시
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
    alertDiv.style.zIndex = '9999';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

// 정산 인쇄
function printSettlement() {
    window.print();
}

// 정산 엑셀 다운로드
function exportSettlement() {
    alert('엑셀 다운로드 기능 (구현 예정)');
}

// ==================== 새로운 함수들 ====================

// 모든 참여자 로드
async function loadAllParticipants() {
    try {
        allParticipants = await fetchAPI('/participants/');
    } catch (error) {
        console.error('참여자 목록 로드 실패:', error);
        showAlert('참여자 목록을 불러오는데 실패했습니다.', 'danger');
    }
}

// 프로젝트 참여자 로드
async function loadProjectParticipants(projectId) {
    try {
        const participants = await fetchAPI(`/projects/${projectId}/participants`);
        
        // 프로젝트 참여자를 projectParticipants에 저장
        projectParticipants = allParticipants.map(p => {
            const projectP = participants.find(pp => pp.participant_id === p.id);
            return {
                ...p,
                selected: !!projectP,
                profit_rate: projectP ? projectP.profit_rate : p.default_profit_rate
            };
        });
        
    } catch (error) {
        console.error('프로젝트 참여자 로드 실패:', error);
        // 참여자가 없을 수도 있으므로 에러는 무시
        projectParticipants = allParticipants.map(p => ({
            ...p,
            selected: false,
            profit_rate: p.default_profit_rate
        }));
    }
}

// 참여자 목록 렌더링
function renderParticipantsList() {
    const container = document.getElementById('project-participants-list');
    
    if (allParticipants.length === 0) {
        container.innerHTML = '<p class="text-muted">등록된 참여자가 없습니다.</p>';
        return;
    }
    
    // 참여자가 선택되지 않았으면 초기화
    if (projectParticipants.length === 0) {
        projectParticipants = allParticipants.map(p => ({
            ...p,
            selected: false,
            profit_rate: p.default_profit_rate
        }));
    }
    
    container.innerHTML = projectParticipants.map((p, index) => `
        <div class="card mb-2">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-md-1">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" 
                                   id="participant-${p.id}" 
                                   ${p.selected ? 'checked' : ''}
                                   onchange="toggleParticipant(${index})">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <label class="form-check-label" for="participant-${p.id}">
                            <strong>${p.name}</strong>
                            <span class="badge bg-secondary ms-2">${p.code}</span>
                        </label>
                        <div class="text-muted small">${getRoleText(p.role)}</div>
                    </div>
                    <div class="col-md-3">
                        <small class="text-muted">기본 수익률: ${p.default_profit_rate}%</small>
                    </div>
                    <div class="col-md-4">
                        <div class="input-group input-group-sm">
                            <span class="input-group-text">수익률 (%)</span>
                            <input type="number" class="form-control" 
                                   id="profit-rate-${p.id}"
                                   value="${p.profit_rate || p.default_profit_rate}"
                                   min="0" max="100" step="0.1"
                                   ${!p.selected ? 'disabled' : ''}
                                   onchange="updateParticipantRate(${index}, this.value)">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

// 참여자 선택/해제
function toggleParticipant(index) {
    projectParticipants[index].selected = !projectParticipants[index].selected;
    const input = document.getElementById(`profit-rate-${projectParticipants[index].id}`);
    input.disabled = !projectParticipants[index].selected;
}

// 참여자 수익률 업데이트
function updateParticipantRate(index, rate) {
    projectParticipants[index].profit_rate = parseFloat(rate);
}

// 역할 텍스트 반환
function getRoleText(role) {
    const roleNames = {
        'admin': '관리자',
        'lead': '팀장',
        'senior': '선임',
        'regular': '일반',
        'assistant': '보조'
    };
    return roleNames[role] || role;
}

// 진도 메모 자동 분석
async function analyzeProgressMemo() {
    const memo = document.getElementById('project-progress-notes').value;
    
    if (!memo || memo.trim() === '') {
        showAlert('진도 메모를 입력해주세요.', 'warning');
        return;
    }
    
    try {
        const result = await fetchAPI('/progress/analyze', {
            method: 'POST',
            body: JSON.stringify({ memo: memo })
        });
        
        // 분석 결과 적용
        if (result.stage) {
            document.getElementById('project-current-stage').value = result.stage;
        }
        if (result.progress_rate !== null && result.progress_rate !== undefined) {
            document.getElementById('project-progress-rate').value = result.progress_rate;
        }
        
        // 프로그레스 바 업데이트
        updateProgressBar();
        
        showAlert(`분석 완료! 단계: ${result.stage}, 진도율: ${result.progress_rate}%`, 'success');
        
    } catch (error) {
        console.error('진도 메모 분석 실패:', error);
        showAlert('진도 메모 분석에 실패했습니다: ' + error.message, 'danger');
    }
}

// 프로그레스 바 업데이트
function updateProgressBar() {
    const stageSelect = document.getElementById('project-current-stage');
    const rateInput = document.getElementById('project-progress-rate');
    const progressBar = document.getElementById('overall-progress-bar');
    const progressText = document.getElementById('overall-progress-text');
    
    // 단계별 기본 진도율
    const stageRates = {
        '아이디어': 5,
        '소개': 10,
        '상담': 20,
        '견적': 30,
        '계약': 40,
        '개발': 60,
        '테스트': 80,
        '납품': 90,
        '완료': 100,
        '유지보수': 100
    };
    
    let rate = 0;
    
    // 진도율 입력값이 있으면 우선 사용
    if (rateInput.value && rateInput.value.trim() !== '') {
        rate = parseFloat(rateInput.value);
    }
    // 없으면 단계에서 추정
    else if (stageSelect.value && stageSelect.value !== '') {
        rate = stageRates[stageSelect.value] || 0;
    }
    
    // 범위 제한
    rate = Math.max(0, Math.min(100, rate));
    
    // 프로그레스 바 업데이트
    if (progressBar && progressText) {
        progressBar.style.width = rate + '%';
        progressText.textContent = rate + '%';
        
        // 색상 변경
        progressBar.className = 'progress-bar progress-bar-striped progress-bar-animated';
        if (rate < 30) {
            progressBar.classList.add('bg-danger');
        } else if (rate < 70) {
            progressBar.classList.add('bg-warning');
        } else if (rate < 100) {
            progressBar.classList.add('bg-info');
        } else {
            progressBar.classList.add('bg-success');
        }
    }
}
