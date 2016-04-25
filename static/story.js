// Aload plugin.  


function aload(nodes) {
    'use strict';

    nodes = nodes || window.document.querySelectorAll('[data-aload]');

    if (nodes.length === undefined) {
        nodes = [nodes];
    }

    var i = 0,
        len = nodes.length,
        node;

    for (i; i < len; i += 1) {
        node = nodes[i];
        node[ node.tagName !== 'LINK' ? 'src' : 'href' ] = node.getAttribute('data-aload');
        node.removeAttribute('data-aload');
    }

    return nodes;
};


window.onload = function() {
    var btns = document.getElementsByTagName('button'),
        len = 2;


    function loads() {
        aload(document.getElementById('async-' + this.id ));
        this.className = 'hide';
    }

    while (len) {
        len -= 1;
        btns[len].onclick = loads;
    }
};


