import React from 'react';
import {Link} from 'react-router-dom';
import './Header.css';

const Header = () => {
    return (
        <div className="Header">
            <Link to="/register" className="item">register</Link>
            <Link to="/maskdetecting" className="item">detecting</Link>
        </div>
    );
};

export default Header;