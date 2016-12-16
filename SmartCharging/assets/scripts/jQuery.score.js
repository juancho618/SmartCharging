/*!
 * Score.js - jQuery Star Rating Plugin
 * Version: 0.0.1-beta
 * Copyright 2013 Haozki
 */

(function($, window, undefined) {
    /* Note:
        1.APIæ–¹æ³•ä¸­çš„thisé€šé€šæŒ‡å‘jQueryå¯¹è±¡ï¼Œå›žè°ƒå‡½æ•°ä»¥åŠç§æœ‰æ–¹æ³•ä¸­çš„thisæŒ‡å‘DOMå¯¹è±¡
        2.è®¾ç½®æ“ä½œå¯¹æ‰€æœ‰é€‰ä¸­çš„jQueryå¯¹è±¡æœ‰æ•ˆï¼ŒèŽ·å–æ“ä½œåªå¯¹jQueryå¯¹è±¡é›†åˆä¸­çš„ç¬¬ä¸€ä¸ªå…ƒç´ æœ‰æ•ˆ
    */
    var methods = {
        /* åˆå§‹åŒ–æ’ä»¶ */
        init: function(option){
            return this.each(function(){
                var _this = this,
                    $this = $(this);
                option = this.option = $.extend({}, $.fn.score.defaults, $this.data(), option); // åœ¨æ”¹å˜this.optionæ—¶åº”è¯¥åŒæ­¥$(this).data('option')

                // ä¿ç•™ä¸€ä»½åŽŸDOMå¯¹è±¡çš„å‰¯æœ¬
                this.raw = $(this).clone()[0];

                var itemType = this.tagName === 'UL' ? 'li' : 'span';
                var items = '';
                for (var i=0; i < option.number; i++)
                {
                    var hint = option.number - i;
                    if (option.hints){
                        hint = option.hints[hint-1] ? option.hints[hint-1] : hint;
                    }
                    items += '<'+ itemType + ' class="score-item" title="' + hint + '"></' +itemType + '>';
                }
                $this.addClass('scorejs').html(items).data('option',option)
                    .css({
                        'font-size': option.size+'px',
                        'color': option.color
                    });

                // è¯»å–æ ¼å¼åŒ–ä¸ºæµè§ˆå™¨DOM Styleå¯¹è±¡ä¸­çš„æ ¼å¼
                this.initStyle = {
                    fontSize: $this.css('font-size'),
                    color: $this.css('color')
                };

                /** è¾“å‡ºè°ƒè¯•ä¿¡æ¯ **/
                debug.call(_this, $this, 'Initialization OptionData: ', option); // æ­¤å¤„DOMä¸Šæ‰æœ‰optionå±žæ€§ï¼Œå¦åˆ™debugé€šè¿‡thisè¯»å–ä¸åˆ°debugé…ç½®é¡¹çš„å€¼

                if (option.readOnly){
                    methods.readOnly.call($this, true);
                }else{
                    methods._binds.call(_this);
                }

                if (option.fontAwesome){
                    $this.addClass('fontawesome');
                }

                if (option.vertical){
                    $this.addClass('score-vertical');
                }

                if (typeof Number(option.score) === 'number'){
                    methods.score.call($this, Number(option.score));
                }
            });
        },
        /* è®¾ç½®/è¿”å›žåˆ†æ•° */
        score: function(score){
            if (score){
                return this.each(function(){
                    var option = this.option;
                    score = score > option.number ? option.number : score;
                    var index = option.number - score;
                    $(this)
                        .children()
                        .removeClass('active')
                        .eq(index)
                        .addClass('active')
                        .nextAll()
                        .addClass('active')
                        .end()
                        .parent('.scorejs')
                        .data({
                            'index': index,
                            'score': score
                        });

                    /** è¾“å‡ºè°ƒè¯•ä¿¡æ¯ **/
                    debug.call(this, $(this), 'Score Set: ', score);
                });
            }else{
                return this.data('score');  // æ³¨æ„ï¼šAPIæ–¹æ³•ä¸­çš„thisç»Ÿä¸€æŒ‡å‘jQueryå¯¹è±¡
            }
        },
        /* è®¾ç½®/è¿”å›žé…ç½®é¡¹ */
        option: function(option){
            if (option){
                return this.each(function(){
                    var oriOption = this.option;
                    var newOption = $.extend({}, oriOption, option);

                    methods.destroy.call($(this));
                    methods.init.call($(this), newOption);

                    /** è¾“å‡ºè°ƒè¯•ä¿¡æ¯ **/
                    debug.call(this, $(this), 'Option Set: ', option, 'Original Option: ', oriOption, 'New Option: ', newOption);
                });
            }else{
                return this.data('option');  // æ³¨æ„ï¼šAPIæ–¹æ³•ä¸­çš„thisç»Ÿä¸€æŒ‡å‘jQueryå¯¹è±¡
            }
        },
        /* è®¾ç½®ä¸ºåªè¯» */
        readOnly: function(readOnly){
            return this.each(function(){
                if (readOnly){
                    // è§£ç»‘åŽè¦è¿˜åŽŸä¹‹å‰çš„åˆ†æ•°ï¼Œåšå®Œmouseoutè¯¥åšçš„äº‹ï¼Œé¿å…åœ¨hoverè¿‡ç¨‹ä¸­è§£ç»‘äº†mouseoutäº‹ä»¶åŽé¼ æ ‡å†ç¦»å¼€ä¸èƒ½æ¢å¤ä¹‹å‰çš„åˆ†æ•°çš„é—®é¢˜
                    $(this)
                        .addClass('read-only')
                        .off('.scorejs')
                        .children()
                        .removeClass('score-item')
                        .addClass('score-item-static')
                        .eq($(this).data('index'))
                        .addClass('active')
                        .nextAll()
                        .addClass('active');
                }else{
                    if ($(this).hasClass('read-only')){
                        $(this)
                            .removeClass('read-only')
                            .children()
                            .removeClass('score-item-static')
                            .addClass('score-item')

                        methods._binds.call(this);
                    }
                }

                /** è¾“å‡ºè°ƒè¯•ä¿¡æ¯ **/
                debug.call(this, $(this), 'readOnly:', readOnly);
            });
        },
        /* å–æ¶ˆå½“å‰çš„è¯„åˆ† */
        cancel: function(){
            return this.each(function(){
                $(this).removeData('index score').children().removeClass('active');

                /** è¾“å‡ºè°ƒè¯•ä¿¡æ¯ **/
                debug.call(this, $(this), 'Canceled');
            });
        },
        /* é”€æ¯æ’ä»¶å®žä¾‹ */
        destroy: function(){
            return this.each(function(){
                // !? è€ƒè™‘æ˜¯å¦éœ€è¦è¿˜åŽŸstyleå±žæ€§
                $(this).off('.scorejs').empty().removeClass('scorejs read-only fontawesome score-vertical').removeData('index score option');

                // å¦‚æžœå½“å‰styleå±žæ€§å€¼ä¸Žé…ç½®é¡¹ä¸åŒï¼Œè¯´æ˜Žæ˜¯åˆå§‹åŒ–åŽåœ¨å…¶ä»–åœ°æ–¹æ‰‹åŠ¨ä¿®æ”¹çš„ï¼Œæ— éœ€è¿˜åŽŸï¼Œå¦åˆ™è¦è¿˜åŽŸæˆåˆå§‹åŒ–å‰å·²ç»è®¾ç½®çš„å€¼
                if (this.style.fontSize === this.initStyle.fontSize){
                    this.style.fontSize = this.raw.style.fontSize;
                }
                if (this.style.color === this.initStyle.color){
                    this.style.color = this.raw.style.color;
                }
                if ($(this).attr('style') === ''){
                    $(this).removeAttr('style');
                }

                /** è¾“å‡ºè°ƒè¯•ä¿¡æ¯ **/
                debug.call(this, $(this), 'Destroyed'); // è¦åœ¨delete this.option;ä¹‹å‰è¾“å‡ºè°ƒè¯•ï¼Œå¦åˆ™debugå‡½æ•°èŽ·å–ä¸åˆ°option

                delete this.option;
            });
        },
        /* ç»‘å®šæ’ä»¶äº‹ä»¶ */
        _binds: function(){
            var _this = this,
                $this = $(this),
                option = this.option;
            /* æ³¨æ„: onäº‹ä»¶ç»‘å®šçš„å‡½æ•°ä¸­çš„thisæŒ‡å‘äº‹ä»¶è§¦å‘çš„DOMå¯¹è±¡ */
            $this.on({
                'click.scorejs': function(event){
                    var score = option.number - $(this).index();
                    methods.score.call($this, score);

                    // è§¦å‘å›žè°ƒå‡½æ•°
                    setCallback.call(_this, event.type, score, event);
                },
                'mouseover.scorejs': function(event){
                    var score = option.number - $(this).index();
                    $this.children().removeClass('active');

                    // è§¦å‘å›žè°ƒå‡½æ•°
                    setCallback.call(_this, event.type, score, event);
                },
                'mouseout.scorejs': function(event){
                    var score = methods.score.call($this);
                    $this.children()
                        .eq($(this).parent().data('index'))
                        .addClass('active')
                        .nextAll()
                        .addClass('active');

                    // è§¦å‘å›žè°ƒå‡½æ•°
                    setCallback.call(_this, event.type, score, event);
                }
            }, '.score-item');
        }
    };

    // å›žè°ƒå‡½æ•°æŽ§åˆ¶ï¼ˆthis -> DOMï¼‰
    function setCallback(callback){
        var callbackReference;
        if (typeof this.option[callback] === 'function'){
            callbackReference = this.option[callback];
            this.option[callback].apply(this, Array.prototype.slice.call(arguments, 1));
        }else{
            callbackReference = 'No callback function set';
        }

        /** è¾“å‡ºè°ƒè¯• */
        debug.call(this, 'Callback Triggered: [',callback,'|',callbackReference,']');
    }

    // è°ƒè¯•å‡½æ•°ï¼ˆthis -> DOMï¼‰
    function debug(){
        if (this.option.debug){
            var logger = window.console['debug'];
            if (typeof logger === 'function'){
                logger.apply(window.console, arguments);
            }
        }
    }

    $.fn.score = function (option) {
        if (methods[option]) {
            return methods[option].apply(this, Array.prototype.slice.call(arguments, 1));
        }else if (typeof option === "object" || !option) {
            return methods.init.apply(this, arguments);
        }
        return false;
    }

    // é»˜è®¤é…ç½®é¡¹
    $.fn.score.defaults = {
        number      : 5,              // è¯„åˆ†èŒƒå›´
        size        : 26,             // å›¾æ ‡å¤§å°
        color       : 'black',        // å›¾æ ‡é¢œè‰²
        score       : undefined,      // åˆå§‹åŒ–æ—¶è¦è®¾ç½®çš„åˆ†æ•°
        vertical    : false,          // åž‚ç›´æ¨¡å¼
        hints       : undefined,      // æ›¿æ¢è¯„åˆ†æ¡ç›®æç¤ºï¼Œä¾‹: ['bad', 'poor', 'regular', 'good', 'gorgeous']ï¼ˆé»˜è®¤æ˜¯ä»Ž1å¼€å§‹çš„é˜¿æ‹‰ä¼¯æ•°å­—ï¼‰
        click       : undefined,      // Callback executed on click.
        mouseover   : undefined,      // Callback executed on mouseover.
        mouseout    : undefined,      // Callback executed on mouseout.
        readOnly    : false,          // åªè¯»ä¸èƒ½è¯„åˆ†
        fontAwesome : false,          // ä½¿ç”¨FontAwesome
        custom      : false,          // è‡ªå®šä¹‰æ¨¡å¼ã€é¢„ç•™ï¼Œç¬¬äºŒç‰ˆä¸­å®žçŽ°ã€‘
        debug       : false           // æ‰“å¼€å¼€å‘è€…è°ƒè¯•
    }
})(jQuery, window);/**
 * Created by Juancho on 12/16/2016.
 */
