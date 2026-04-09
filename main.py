:root {
    --primary: #7B3FD0;
    --dark-bg: #1A0F38;
    --light-bg: #F4F2FB;
    --text-main: #1A0F38;
    --text-muted: #7B6FAA;
    --danger: #E85C6A;
    --success: #5DCB8A;
    --warning: #F0AA30;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', sans-serif; background: var(--light-bg); color: var(--text-main); }

.container { display: flex; min-height: 100vh; }

/* Sidebar */
.sidebar { width: 240px; background: var(--dark-bg); color: white; display: flex; flex-direction: column; }
.logo-section { padding: 24px; display: flex; align-items: center; gap: 12px; }
.logo-icon { width: 36px; height: 36px; background: var(--primary); border-radius: 10px; position: relative; }
.logo-text { font-weight: 700; font-size: 14px; }
.logo-subtext { font-size: 10px; color: var(--text-muted); }

.nav-menu { flex: 1; padding: 10px; }
.nav-item { 
    display: flex; align-items: center; padding: 12px 16px; 
    color: #BFA4EC; text-decoration: none; border-radius: 8px; margin-bottom: 4px;
}
.nav-item.active { background: var(--primary); color: white; }
.badge { background: var(--danger); padding: 2px 8px; border-radius: 10px; font-size: 10px; margin-left: auto; }

.sidebar-user { background: #0D0720; padding: 15px; display: flex; align-items: center; gap: 10px; }
.avatar { width: 36px; height: 36px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; }

/* Main Content */
.main-content { flex: 1; padding: 24px; overflow-y: auto; }
.topbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
.breadcrumb { font-size: 12px; color: #B0A4D4; }
.search-bar { padding: 8px 16px; border-radius: 20px; border: 1px solid #EDE9F8; background: #FFF; width: 240px; }

/* Grid & Cards */
.metrics-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 24px; }
.card { background: white; border-radius: 14px; padding: 20px; position: relative; overflow: hidden; }
.metric { border-top: 5px solid; }
.metric.purple { border-color: var(--primary); }
.metric.red { border-color: var(--danger); }
.metric.orange { border-color: var(--warning); }
.metric.dark { border-color: #9B72E0; background: var(--dark-bg); color: white; }

.label { font-size: 12px; color: var(--text-muted); display: block; }
.value { font-size: 32px; font-weight: 700; margin: 8px 0; display: block; }
.trend { font-size: 11px; }
.trend.up { color: var(--success); }

/* Room Grid */
.content-row { display: grid; grid-template-columns: 2fr 1.2fr; gap: 20px; }
.room-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; }
.room-item { padding: 15px; border-radius: 12px; border-top: 4px solid; }
.room-item.empty { background: #F0EBFC; border-color: var(--primary); }
.room-item.busy { background: #FDF0F1; border-color: var(--danger); }
.room-item.maintenance { background: #FEF6E6; border-color: var(--warning); }

.status-tag { padding: 4px 12px; border-radius: 12px; font-size: 10px; font-weight: 700; display: inline-block; margin-top: 10px; }
.status-tag.success { background: #D9F5E8; color: #1A7A4A; }
.status-tag.danger { background: #F9CDD1; color: #C0384A; }
.status-tag.warning { background: #FCDFA0; color: #8A5508; }

/* Progress Bar */
.utilization { margin-top: 30px; }
.progress-bar { height: 8px; background: #EDE9F8; border-radius: 4px; margin-top: 8px; }
.progress { height: 100%; background: var(--primary); border-radius: 4px; }

/* Booking List */
.booking-item { background: #F9F7FE; padding: 15px; border-radius: 10px; margin-top: 10px; border-left: 4px solid; display: flex; justify-content: space-between; align-items: center; }
.purple-line { border-color: var(--primary); }
.red-line { border-color: var(--danger); }
.time-left { font-size: 10px; color: #B0A4D4; }