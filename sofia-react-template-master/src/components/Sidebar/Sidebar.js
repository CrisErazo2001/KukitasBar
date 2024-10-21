import React, { useEffect, useState } from 'react';
import { logoutUser } from "../../actions/auth";
import logoutIcon from "../../assets/navbarMenus/pfofileIcons/logoutBlack.svg";
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
//import { Button} from 'reactstrap';
import { withRouter, Link } from 'react-router-dom';
import s from "./Sidebar.module.scss";
import LinksGroup from "./LinksGroup/LinksGroup.js";
import { changeActiveSidebarItem } from "../../actions/navigation.js";
import SofiaLogo from "../Icons/SofiaLogo.js";
import NewUser from "../../assets/person-add.svg"
import cn from "classnames";

const Sidebar = (props) => {

  const {
    activeItem = '',
    ...restProps
  } = props;

  const [burgerSidebarOpen, setBurgerSidebarOpen] = useState(false)

  useEffect(() => {
    if (props.sidebarOpened) {
      setBurgerSidebarOpen(true)
    } else {
      setTimeout(() => {
        setBurgerSidebarOpen(false)
      }, 0);
    }
  }, [props.sidebarOpened])

  const doLogout = () => {
    props.dispatch(logoutUser());
  }

  return (
    <nav className={cn(s.root, {[s.sidebarOpen]: burgerSidebarOpen})} >
      <header className={s.logo}>
        <SofiaLogo/>
        <span className={s.title}>SOFIA</span>
      </header>
      <ul className={s.nav}>
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="Dashboard"
          isHeader
          iconName={<i className={'eva eva-home-outline'}/>}
          link="/template/dashboard"
          index="dashboard"
          badge="9"
        />
        <Link to="/register">
          <div className={s.linkR}>
            <img className={s.logoutIcon} src={NewUser} alt="Logout" />  
            <h6 className='pt-2'>Crear Usuario</h6>
          </div>
        </Link>
        <h5 className={s.navTitle}>TEMPLATE</h5>
        {/* 
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="Typography"
          isHeader
          iconName={<i className={'eva eva-text-outline'}/>}
          link="/template/typography"
          index="typography"
        />
        */}
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="Ingredientes"
          isHeader
          iconName={<i className={'eva eva-layers'}/>}
          link="/template/ingredientes"
          index="ingredientes"
        />
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="Distribución"
          isHeader
          iconName={<i className={'eva eva-layout'}/>}
          link="/template/distribucion"
          index="ingredientes"
        />
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="Recetas"
          isHeader
          iconName={<i className={'eva eva-list'}/>}
          link="/template/recetas"
          index="ingredientes"
        />
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="Listado de Pedidos"
          isHeader
          iconName={<i className={'eva eva-grid-outline'}/>}
          link="/template/tables"
          index="tables"
        />
        
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="Notifications"
          isHeader
          iconName={<i className={'eva eva-bell-outline'}/>}
          link="/template/notifications"
          index="notifications"
        />
        <LinksGroup
          onActiveSidebarItemChange={activeItem => props.dispatch(changeActiveSidebarItem(activeItem))}
          activeItem={props.activeItem}
          header="UI Elements"
          isHeader
          iconName={<i className={'eva eva-cube-outline'}/>}
          link="/template/uielements"
          index="uielements"
          childrenLinks={[
            {
              header: 'Charts', link: '/template/ui-elements/charts',
            },
            {
              header: 'Icons', link: '/template/ui-elements/icons',
            },
            {
              header: 'Google Maps', link: '/template/ui-elements/maps',
            },
          ]}
        />
      </ul>


      <div className="bg-widget d-flex flex-row  mt-auto ml-1" onClick={() => doLogout()} href="#">
        <button className={s.logout} type="submit">
          <img className={s.logoutIcon} src={logoutIcon} alt="Logout" />
          <span className="ml-1">Logout</span>
        </button>
      </div>
    </nav>
  );
}

Sidebar.propTypes = {
  sidebarOpened: PropTypes.bool,
  dispatch: PropTypes.func.isRequired,
  activeItem: PropTypes.string,
  location: PropTypes.shape({
    pathname: PropTypes.string,
  }).isRequired,
}

function mapStateToProps(store) {
  return {
    sidebarOpened: store.navigation.sidebarOpened,
    activeItem: store.navigation.activeItem,
  };
}

export default withRouter(connect(mapStateToProps)(Sidebar));
