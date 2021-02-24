import { createRouter, createWebHistory } from "vue-router";

import DcHeros from './pages/DcHeros';
import Calendar from './pages/Calendar';
import Home from './pages/Home';
import Markdown from './pages/Markdown';
import Slider from './pages/Slider';
import Calculator from './pages/Calculator';
import ReuseableModal from './pages/ReusableModal';

const routes = [
    {path: '/', component:Home},
    {path: '/dc-heros', component:DcHeros},
    {path: '/calendar', component:Calendar},
    {path: '/markdown', component:Markdown},
    {path: '/slider-carousel', component:Slider},
    {path: '/calculator', component:Calculator},
    {path: '/resuseable-modal', component:ReuseableModal},

];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;