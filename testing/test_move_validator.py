from utils.card_logic.move_validator import is_move_valid

def test() -> None:
        """

    // Parameters:
    //      1. rule: global game rules
    //      2. rank: current rank
    //      3. trumpSuit: current trump suit
    //      4. firstPlaySuit: the suit of the initial player's cards, should be a value returned by getCardSuit()
    //      5. firstPlayPattern: the initial player's card pattern
    //      6. cardToPlay: card to be played by the current player, pre-sorted
    //      7. currentHands: the remaining hand of the current player, pre-sorted
    //
        """
        """

        let game = { status: {}, rule: {} };
        game.rule = { H5: false, startingRank: 9, turbo: true, cardSet: 4, dealAll: false, trumpSuit: true, rankJoker: true };
        variable.checkVersionCompliance(game);
        let rule = game.rule;

        //test cases for initial play...
        //test case 1, one card
        expect(cardRules.firstPlayValid(rule, 9, "S", ["DT"], [[], [], [], [], [], []])).to.equal(true);
        //test case 2, one card, rank
        expect(cardRules.firstPlayValid(rule, "T", "S", ["DT"], [[], [], [], [], [], []])).to.equal(true);
        //test case 3, one card, joker
        expect(cardRules.firstPlayValid(rule, "T", "S", ["JB"], [[], [], [], [], [], []])).to.equal(true);
        //test case 6, 3 cards, different suit
        expect(cardRules.firstPlayValid(rule, "T", "S", ["H3", "SA", "SA"], [[], [], [], [], []])).to.equal(false);
        //test case 7, one double, legal play
        expect(cardRules.firstPlayValid(rule, "T", "C", ["S3", "S3"], [[], ["S5", "S5", "S7"], [], [], []])).to.equal(true);
        //test case 8, one double tractor, legal play
        expect(cardRules.firstPlayValid(rule, "T", "C", ["S3", "S3", "S2", "S2"], [[], ["S5", "S5", "S7"], [], [], []])).to.equal(true);
        //test case 9, one triple, legal play
        expect(cardRules.firstPlayValid(rule, "T", "C", ["S3", "S3", "S3"], [[], ["S5", "S5", "S5"], [], [], []])).to.equal(true);
        //test case 10, one triple tractor, legal play
        expect(cardRules.firstPlayValid(rule, "T", "C", ["S3", "S3", "S3", "S2", "S2", "S2"], [[], ["S5", "S5", "S5"], ["S7", "S7", "S7", "S6", "S6", "S6"], [], []])).to.equal(true);
        //test case 11, one quad, legal play
        expect(cardRules.firstPlayValid(rule, "T", "C", ["S3", "S3", "S3", "S3"], [[], ["S5", "S5", "S5", "S5"], ["S7", "S7", "S7", "S6", "S6", "S6"], [], []])).to.equal(true);
        //test case 12, one quad tractor, legal play
        expect(cardRules.firstPlayValid(rule, "T", "C", ["S3", "S3", "S3", "S3", "S2", "S2", "S2", "S2"], [[], ["S5", "S5", "S5", "S5"], ["S7", "S7", "S7", "S6", "S6", "S6"], [], []])).to.equal(true);
        //test case 13, one double and one single, legal play
        expect(cardRules.firstPlayValid(rule, "T", "C", ["SJ", "S3", "S3"], [[], ["S5", "S4", "S3", "S2"], ["C7", "C7", "C7", "C6", "C6", "C6"], [], []])).to.equal(true);
        //test case 14, one double and one single, illegal play due to single
        expect(cardRules.firstPlayValid(rule, "T", "C", ["SJ", "S3", "S3"], [[], ["SK", "S4", "S3", "S2"], ["C7", "C7", "C7", "C6", "C6", "C6"], [], []])).to.equal(false);
        //test case 15, one double and one single, illegal play due to double
        expect(cardRules.firstPlayValid(rule, "T", "C", ["SJ", "S3", "S3"], [[], ["C7", "C7", "C7", "C6", "C6", "C6"], [], [], ["S4", "S4", "S4", "S2"]])).to.equal(false);
        //test case 16, one double and one triple, illegal play due to double
        expect(cardRules.firstPlayValid(rule, "T", "C", ["SK", "SK", "SJ", "SJ", "SJ"], [[], ["C7", "C7", "C7", "C6", "C6", "C6"], [], [], ["SA", "SA", "S2"]])).to.equal(false);
        //test case 17, one double and one quad, illegal play due to double
        expect(cardRules.firstPlayValid(rule, "T", "C", ["SK", "SK", "SK", "SK", "S9", "S9"], [[], ["C7", "C7", "C7", "C6", "C6", "C6"], [], [], ["SA", "SA", "S2"]])).to.equal(false);
        expect(cardRules.firstPlayValid(rule, "2", "D", ["SA", "SK", "SQ", "SQ"], [[], ["SJ", "ST", "ST", "ST", "S8", "S8"]])).to.equal(true);
        //test case 18, trump two doubles, illegal play due to smaller double
        expect(cardRules.firstPlayValid(rule, "T", "S", ["ST", "ST", "SK", "SK"], [[], ["C7", "C7", "C7", "C6", "C6", "C6"], [], [], ["DT", "DT", "S2", "S2", "S2", "D7"]])).to.equal(false);
        expect(cardRules.firstPlayValid(rule, "9", "S", ["D9", "D9", "SA", "SA"], [[], ["JR", "JR", "JR", "JB", "JB", "JB"], [], [], ["DT", "DT", "S2", "S2", "S2", "D7"]])).to.equal(true);
        expect(cardRules.firstPlayValid(rule, "", "S", ["D9", "D9", "SA", "SA"], [[], ["JR", "JR", "JR", "JB", "JB", "JB"], [], [], ["DT", "DT", "S2", "S2", "S2", "D7"]])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["CQ", "CQ", "D3", "D2"], ["CA", "CA", "CQ", "CQ", "C5", "C3", "C2", "D3", "D2"])).to.equal(false);
        expect(cardRules.firstPlayValid(rule, "", "D", ["SA", "SQ", "SQ", "SJ", "SJ", "ST", "ST", "ST"], [[], ["SK", "SK"], ["SA", "S7", "S7", "S6", "S6", "S6"], [], []])).to.equal(true);
        var forcedOutCards = [];
        expect(cardRules.firstPlayValid(game.rule, "T", "C", ["SA", "SJ", "SJ"], [[], ["SA", "SQ", "SQ", "S2"], [], []], forcedOutCards)).to.equal(false);
        expect(JSON.stringify(forcedOutCards)).to.equal('["SJ","SJ"]');
        expect(cardRules.firstPlayValid(game.rule, "T", "C", ["SK", "SJ", "SJ"], [[], ["SA", "SK", "SQ", "S2"], [], []], forcedOutCards)).to.equal(false);
        expect(JSON.stringify(forcedOutCards)).to.equal('["SK"]');
        rule = { "turbo": false, "showBottomCards": false, "powerSeatA": true, "H5": false, "startingRank": "2", "lastRoundWinScore": "30", "riseRankLimit": "3", "cardEnforce": "1", "cardSet": "3", "dealAll": true, "openTimeSpan": "12", "observerAllowed": false, "turboSameSuit": false, "trumpSuit": false, "rankJoker": false, "randomSeat": false, "secondBeforeBottomCards": 0, "timeout": 5 };
        expect(cardRules.firstPlayValid(rule, "3", "D", ["SA", "SA", "S6", "S6", "S5", "S5"], [["S3", "DQ", "DJ", "D9", "D7", "D6", "D6", "SK", "SK", "SJ", "ST", "ST", "S8", "S7", "S6", "S4", "HA", "HA", "CK", "CT", "C5"], ["D3", "H3", "DA", "DK", "DK", "DT", "D9", "D8", "D5", "D5", "S8", "S2", "HJ", "HJ", "H8", "H7", "H7", "H4", "H2", "C4", "C2"], ["JR", "JR", "JB", "JB", "S3", "S3", "H3", "DA", "D9", "D5", "SA", "SQ", "S9", "S5", "HK", "HQ", "H9", "H9", "H6", "H5", "C5"], ["JR", "JB", "D3", "DJ", "D7", "D2", "SK", "SJ", "S9", "S9", "S8", "S7", "S4", "S2", "S2", "HQ", "H8", "H8", "H7", "H6", "H4"], ["H3", "DK", "DQ", "DQ", "DJ", "D8", "SQ", "SQ", "ST", "S7", "S4", "HA", "HK", "HQ", "HT", "H6", "H5", "H5", "H2", "H2", "CQ"]])).to.equal(true);
        expect(cardRules.firstPlayValid(rule, "4", "H", ["CA", "CQ", "CQ", "C6", "C6", "C5", "C5"], [[], ["CA", "CK", "CT", "CT", "C9", "C8", "C3", "C3", "C2"], [], [], []])).to.equal(true);
        expect(cardRules.firstPlayValid(rule, "T", "J", ["SA", "S8", "S8", "S7", "S7", "S6", "S6"], [["SA", "SA", "SK", "SJ", "SJ", "S9", "S9", "S8"], [], []])).to.equal(true);
        rule = { "powerSeatA": true, "cardEnforce": 1, "observerAllowed": true, "secondBeforeBottomCards": 12, "turbo": false, "showBottomCards": false, "H5": false, "startingRank": 2, "lastRoundWinScore": 30, "riseRankLimit": 3, "cardSet": 3, "dealAll": false, "openTimeSpan": 744, "timeout": 30, "kickPlayer": 1, "trumpSuit": false, "mixJoker": 2, "gameTime": 0, "cutCards": true, "replayAllowed": true, "playCardReminder": 15, "turboSameSuit": false, "rankJoker": false, "randomSeat": false, "feedbackAllowed": false };
        expect(cardRules.followPlayValid(rule, "4", "D", "S", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [] }, ["HQ", "CQ", "CJ"], ["JR", "S4", "H4", "C4", "HK", "HQ", "H5", "CK", "CQ", "CJ", "CT"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "9", "H", "S", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [2], single: [] }, ["S5", "S5", "S5", "S3", "S3"], ["S5", "S5", "S5", "S3", "S3", "S2", "S2", "S2"])).to.equal(true);

        //test cases for following play...
        //test case 1, three cards, all singles
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [], single: [1, 1, 1] }, ["CT", "CK", "CA"], ["C2", "CT", "CK", "CA", "D5", "H2", "H4", "SK", "C9", "C9", "JR"])).to.equal(true);
        //test case 2, three cards, all singles, less or equal in hand, forcing but cheating
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [], single: [1, 1, 1] }, ["CT", "CK", "DT"], ["CT", "CK", "CA", "DT", "H2", "H4", "SK", "C9", "C9", "JR"])).to.equal(false);
        //test case 3, three cards, all singles, more in hand, not forcing but cheating
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [], single: [1, 1, 1] }, ["CT", "CK", "DT"], ["C2", "CT", "CK", "CA", "DT", "H2", "H4", "SK", "D9", "D9", "JR"])).to.equal(false);
        //test case 4, one single one double, cheating by hiding double
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [2], single: [1] }, ["C2", "CT", "CA"], ["C2", "CT", "CK", "CK", "CA"])).to.equal(false);
        //test case 5, two doubles, cheating by hiding one double
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [2, 2], single: [] }, ["C2", "C2", "C4", "CA"], ["C2", "C2", "C4", "CT", "CK", "CK", "CA"])).to.equal(false);
        //test case 6, double tractor, legal play one double two single
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["C2", "C2", "C4", "CA"], ["C2", "C2", "C4", "CT", "CK", "CA"])).to.equal(true);
        //test case 7, double tractor, legal play hiding a triple
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["CT", "CK", "CK", "CA"], ["C2", "C2", "C2", "CT", "CK", "CK", "CA"])).to.equal(true);
        //test case 8, double tractor, legal play one double two single, spliting a triple
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["C2", "C2", "CK", "CA"], ["C2", "C2", "CK", "CK", "CK", "CA"])).to.equal(true);
        //test case 9, double tractor of length 3, legal play splitting a quad
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [6], double: [], single: [] }, ["C2", "C2", "C4", "C6", "CK", "CK"], ["C2", "C2", "C4", "C6", "CK", "CK", "CK", "CK"])).to.equal(true);
        //test case 10, double tractor of length 4, legal play splitting a quad
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [8], double: [], single: [] }, ["C2", "C3", "C4", "C5", "CK", "CK", "CK", "CK"], ["C2", "C2", "C2", "C2", "C3", "C4", "C5", "CK", "CK", "CK", "CK"])).to.equal(true);
        //test case 11, one triple, cheating by hiding triple
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [] }, ["C3", "C4", "C5"], ["C2", "C2", "C2", "C2", "C3", "C4", "C5", "CK", "CK", "CK"])).to.equal(false);
        //test case 12, one triple, legal play by giving up a quad
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [] }, ["C2", "C2", "C2"], ["C2", "C2", "C2", "C2", "C3", "C4", "C5", "CK", "CK", "CK"])).to.equal(true);
        //test case 13, one triple, legal play all single
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [] }, ["C2", "C4", "CJ"], ["C2", "C4", "C5", "CT", "CJ", "CA"])).to.equal(true);
        //test case 14, one triple, legal play all single and hide quad
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [] }, ["C2", "C4", "CJ"], ["C2", "C4", "C5", "CT", "CT", "CT", "CT", "CJ", "CA"])).to.equal(true);
        //test case 15, triple tractor, cheating by hiding a double
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [6], triple: [], doubletractor: [], double: [], single: [] }, ["C2", "C2", "C5", "CJ", "CQ", "CA"], ["C2", "C2", "C5", "CT", "CT", "CJ", "CQ", "CA"])).to.equal(false);
        //test case 16, triple tractor, cheating by hiding a triple
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [6], triple: [], doubletractor: [], double: [], single: [] }, ["C2", "C2", "C5", "CJ", "CJ", "CA"], ["C2", "C2", "C5", "CT", "CT", "CT", "CJ", "CJ", "CA"])).to.equal(false);
        //test case 17, triple and double, cheating by hiding a double
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [2], single: [] }, ["C2", "C2", "CT", "CQ", "CA"], ["C2", "C2", "C5", "CT", "CT", "CQ", "CA"])).to.equal(false);
        //test case 18, triple and double, legal play hiding second triple
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [2], single: [] }, ["C2", "C2", "C2", "CQ", "CA"], ["C2", "C2", "C2", "CT", "CT", "CT", "CQ", "CA"])).to.equal(true);
        //test case 19, quad, legal play giving up quad
        expect(cardRules.followPlayValid(rule, 9, "S", "T", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [], double: [], single: [] }, ["C9", "C9", "C9", "C9"], ["S5", "SA", "C9", "C9", "C9", "C9", "D9", "D9", "JR", "JR", "JR"])).to.equal(true);
        //test case 20, quad, legal play giving up a triple
        expect(cardRules.followPlayValid(rule, 9, "S", "T", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [], double: [], single: [] }, ["SA", "C9", "C9", "C9"], ["S5", "SA", "C9", "C9", "C9", "D9", "D9", "JR", "JR", "JR"])).to.equal(true);
        //test case 21, quad, legal play giving up two doubles
        expect(cardRules.followPlayValid(rule, 9, "S", "T", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [], double: [], single: [] }, ["SA", "SA", "C9", "C9"], ["S5", "SA", "C9", "C9", "D9", "D9", "JR"])).to.equal(true);
        //test case 22, quad, cheating by hiding quad
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [], double: [], single: [] }, ["C2", "C2", "C2", "CA"], ["C2", "C2", "C2", "CT", "CT", "CT", "CT", "CA", "CA"])).to.equal(false);
        //test case 23, quad, cheating by hiding triple
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [], double: [], single: [] }, ["C2", "C2", "CA", "CA"], ["C2", "C2", "C4", "CT", "CT", "CT", "CA", "CA"])).to.equal(false);
        //test case 24, quad, cheating by hiding one double
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [], double: [], single: [] }, ["C2", "C2", "C4", "CA"], ["C2", "C2", "C4", "CT", "CA", "CA"])).to.equal(false);
        //test case 25, one quad two triple, cheating by hiding one double, satisfing all triples
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [4], tripletractor: [], triple: [3, 3], doubletractor: [], double: [], single: [] }, ["C2", "C2", "C2", "C4", "CT", "CT", "CT", "CQ", "CQ", "CA"], ["C2", "C2", "C2", "C4", "CT", "CT", "CT", "CQ", "CQ", "CK", "CK", "CA"])).to.equal(false);
        //test case 26, one quad two triple, cheating by hiding one double, not satisfying all triples
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [], quad: [4], tripletractor: [], triple: [3, 3], doubletractor: [], double: [], single: [] }, ["C2", "C2", "C2", "C4", "CT", "CT", "CJ", "CQ", "CQ", "CA"], ["C2", "C2", "C2", "C4", "CT", "CT", "CJ", "CQ", "CQ", "CK", "CK", "CA"])).to.equal(false);
        //test case 27, mother of all bomb case, cheating by hiding one double
        expect(cardRules.followPlayValid(rule, 9, "S", "C", { quadtractor: [8], quad: [4], tripletractor: [6], triple: [], doubletractor: [4], double: [], single: [1] }, ["C2", "C2", "C2", "C3", "C4", "C5", "C6", "C6", "C6", "C7", "C8", "C8", "CT", "CT", "CT", "CT", "CJ", "CJ", "CJ", "CK", "CK", "CK", "CA"], ["C2", "C2", "C2", "C3", "C3", "C4", "C4", "C5", "C6", "C6", "C6", "C7", "C7", "C8", "C8", "CT", "CT", "CT", "CT", "CJ", "CJ", "CJ", "CQ", "CQ", "CK", "CK", "CK", "CA", "CA"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, 2, "D", "S", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [], single: [1] }, ["ST"], ["JR", "H2", "DJ", "DT", "DT", "D9", "D6", "D4", "S9", "HJ", "H4", "CA"])).to.equal(true);
        //test case 28, production false alarm
        expect(cardRules.followPlayValid(rule, 4, "S", "H", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["HQ", "HT", "HT", "H9"], ["HQ", "HT", "HT", "H9", "H7", "H7", "H7", "H2", "H2", "H2"])).to.equal(true);
        //test case 29, production false alarm reverse
        expect(cardRules.followPlayValid(rule, 4, "S", "H", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["HQ", "HT", "HT", "H9"], ["HQ", "HT", "HT", "H9", "H7", "H7", "H7", "H2", "H2"])).to.equal(false);
        rule = { "H5": true, "turbo": true, "cardsSet": 4, "startingRank": 9, "dealAll": true, "rankJoker": true, "lastRoundwinScore": 0, "riseRankLimit": 0, "showBottomCards": true, "cardEnforce": 1, "randomSeat": false, "powerSeatA": false };
        expect(cardRules.followPlayValid(rule, "J", "C", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [], single: [1] }, ["C4"], ["JR", "JR", "JB", "JB", "DJ", "SJ", "DA", "DA", "D9", "D8", "C4", "C4"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["CQ", "CQ", "C3", "C2"], ["CA", "CA", "CQ", "CQ", "C5", "C3", "C2"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "K", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["S9", "S3", "DJ", "CT"], ["JB", "JB", "HA", "HQ", "HT", "H8", "H7", "H2", "H2", "SQ", "ST", "S9", "S5", "S3", "DJ", "DT", "CT"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["CT", "CT", "CT", "C3"], ["CT", "CT", "CT", "C8", "C8", "C3", "C2"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["C5", "C5", "C7", "C7"], ["C7", "C7", "C6", "C6", "C5", "C5"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "9", "H", "S", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [1] }, ["ST", "ST", "C8", "C8"], ["ST", "ST", "C8", "C8", "C6"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "2", "H", "H", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["H5", "H5", "H7", "H7"], ["S2", "S2", "HA", "HA", "H7", "H7", "H5", "H5"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "2", "H", "H", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["S2", "S2", "HA", "HA"], ["S2", "S2", "HA", "HA", "H7", "H7", "H5", "H5"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "9", "H", "S", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [], double: [], single: [] }, ["S6", "S6", "S5", "S5"], ["ST", "ST", "S6", "S6", "S5", "S5"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "K", "H", "C", { quadtractor: [], quad: [], tripletractor: [6], triple: [], doubletractor: [], double: [], single: [] }, ["CA", "CK", "C4", "C4", "C2", "C2"], ["CA", "CK", "C4", "C4", "C3", "C3", "C2", "C2"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "K", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [1] }, ["C3", "C3", "C2", "C2"], ["C4", "C4", "C3", "C3", "C2", "C2"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "T", "H", "C", { quadtractor: [], quad: [], tripletractor: [6], triple: [], doubletractor: [], double: [], single: [] }, ["CA", "CK", "C3", "C3", "C2", "C2"], ["CA", "CK", "C4", "C4", "C3", "C3", "C2", "C2"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "T", "H", "C", { quadtractor: [], quad: [], tripletractor: [6], triple: [], doubletractor: [], double: [], single: [] }, ["CA", "CK", "C4", "C4", "C2", "C2"], ["CA", "CK", "C4", "C4", "C3", "C3", "C2", "C2"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "9", "H", "S", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [6], double: [], single: [] }, ["S8", "S8", "S7", "S7", "S4", "S4"], ["S8", "S8", "S7", "S7", "S5", "S5", "S4", "S4"])).to.equal(true);
        rule = { "turbo": true, "showBottomCards": true, "powerSeatA": true, "H5": false, "startingRank": 5, "lastRoundWinScore": 20, "riseRankLimit": 3, "cardEnforce": 14, "cardSet": 4, "dealAll": true, "openTimeSpan": 744, "trumpSuit": true, "secondBeforeBottomCards": 0, "timeout": 30, "mixJoker": "0", "gameTime": 0, "kickPlayer": 1, "observerAllowed": true, "cutCards": true, "oppTrumpOnly": false, "playCardReminder": 0, "randomSeat": false, "players4_cardSet": 3, "players4_winThreadHold": 80, "players4_lastRoundWinScore": 0, "players4_scorePerRank": 40, "players4_riseRankLimit": 0, "players4_ot_plus": 0, "players5_cardSet": 3, "players5_winThreadHold": 120, "players5_lastRoundWinScore": 0, "players5_scorePerRank": 60, "players5_riseRankLimit": 2, "players5_ot_plus": 1, "players7_cardSet": 4, "players7_winThreadHold": 170, "players7_lastRoundWinScore": 0, "players7_scorePerRank": 80, "players7_riseRankLimit": 0, "players7_ot_plus": 1, "gameMode": 1, "players4": true, "players5": true, "players6": true, "players7": true, "turboSameSuit": false, "rankJoker": false, "replayAllowed": false, "feedbackAllowed": false, "preset": 0, "ABRoom": 0, "ABRoomForever": 0, "AI": 0 }
        expect(JSON.stringify(cardRules.getCardsPattern(rule, '7', "C", ["C6", "C6", "C5", "C5", "C4", "C4"]))).to.equal(`{"single":[],"double":[],"doubletractor":[6],"triple":[],"tripletractor":[],"quad":[],"quadtractor":[]}`);
        expect(cardRules.followPlayValid(rule, "7", "C", "J", cardRules.getCardsPattern(rule, '7', "C", ["C6", "C6", "C5", "C5", "C4", "C4"]), ["C7", "C9", "C9", "C9", "C8", "C8"], ["JR", "C7", "CK", "C9", "C9", "C9", "C8", "C8", "HJ", "HT", "HT", "H9", "H5", "H3", "H3", "ST", "S5"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "7", "C", "J", cardRules.getCardsPattern(rule, '7', "C", ["C6", "C6", "C5", "C5", "C4", "C4"]), ["JR", "C7", "CK", "C9", "C8", "C8"], ["JR", "C7", "CK", "C9", "C9", "C9", "C8", "C8", "HJ", "HT", "HT", "H9", "H5", "H3", "H3", "ST", "S5"])).to.equal(true);
        rule = { "gameMode": 1, "turbo": true, "showBottomCards": true, "powerSeatA": false, "H5": true, "startingRank": 9, "lastRoundWinScore": 0, "riseRankLimit": 0, "cardEnforce": 14, "cardSet": 4, "dealAll": true, "trumpSuit": true, "secondBeforeBottomCards": 15, "timeout": 20, "mixJoker": "2", "gameTime": 0, "kickPlayer": 2, "observerAllowed": true, "cutCards": true, "oppTrumpOnly": true, "playCardReminder": 15, "randomSeat": false, "players4_cardSet": 2, "players4_winThreadHold": 80, "players4_lastRoundWinScore": 0, "players4_scorePerRank": 40, "players4_riseRankLimit": 0, "players4_ot_plus": 0, "players5_cardSet": 3, "players5_winThreadHold": 130, "players5_lastRoundWinScore": 0, "players5_scorePerRank": 60, "players5_riseRankLimit": 0, "players5_ot_plus": 0, "players7_cardSet": 4, "players7_winThreadHold": 170, "players7_lastRoundWinScore": 0, "players7_scorePerRank": 80, "players7_riseRankLimit": 0, "players7_ot_plus": 0, "noTrumpNoTurbo": true, "showQuickTrumpBar": true, "leadWrongCardPoints": 10, "followWrongCardPoints": 10, "winThreadHold": 0, "scorePerRank": 0, "ot_plus": 0, "trumpCallSameSuit": false, "mustPassRank": ["T", "A"], "trumpSuitJReduce": 6, "noTrumpSuitJReduce": 3, "players4": true, "players5": true, "players6": true, "players7": true, "turboSameSuit": false, "rankJoker": false, "openTimeSpan": 12, "replayAllowed": false, "feedbackAllowed": false, "preset": 0, "ABRoom": 0, "ABRoomForever": 0, "AI": 0, "second4Turbo": 15 }
        expect(cardRules.followPlayValid(rule, "9", "S", "C", cardRules.getCardsPattern(rule, '9', "S", ["CJ", "CJ", "CJ", "CT", "CT", "CT"]), ["C5", "C5", "C4", "C4", "C3", "C3"], ["JR", "JR", "S9", "H9", "H9", "C9", "ST", "ST", "S2", "S2", "HT", "H8", "H7", "H6", "H3", "H3", "H2", "CA", "CA", "CQ", "C5", "C5", "C4", "C4", "C3", "C3", "C2", "C2", "DA", "DT", "DT", "D4", "D4", "D3", "D3"])).to.equal(true);
        rule.std = 1; //国标
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [0], double: [2], single: [] }, ["C3", "C2"], ["CQ", "CQ", "CQ", "C3", "C2"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [0], double: [2, 2], single: [] }, ["C3", "C3", "C5", "C6"], ["CQ", "CQ", "CQ", "C3", "C3", "C5", "C6"])).to.equal(false);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [] }, ["C3", "C3", "C2", "C2"], ["CQ", "CQ", "CQ", "CQ", "C3", "C3", "C2", "C2"])).to.equal(false);
        rule.std = 0; //华标
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [0], double: [2], single: [] }, ["C3", "C2"], ["CQ", "CQ", "CQ", "C3", "C2"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [0], double: [2, 2], single: [] }, ["C3", "C3", "C5", "C6"], ["CQ", "CQ", "CQ", "C3", "C3", "C5", "C6"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "4", "H", "C", { quadtractor: [], quad: [], tripletractor: [], triple: [3], doubletractor: [], double: [], single: [] }, ["C3", "C3", "C2", "C2"], ["CQ", "CQ", "CQ", "CQ", "C3", "C3", "C2", "C2"])).to.equal(true);
        //红五四副牌炒地皮
        rule = { "H5": true, "turbo": true, "turboSameSuit": false, "startingRank": 5, "dealAll": true, "trumpSuit": true, "rankJoker": false, "showBottomCards": true, "randomSeat": false, "powerSeatA": false, "cardEnforce": 14, "observerAllowed": true, "openTimeSpan": 744, "secondBeforeBottomCards": 12, "timeout": 20, "mixJoker": "0", "gameTime": 0, "kickPlayer": 2, "cutCards": true, "replayAllowed": false, "playCardReminder": 30, "feedbackAllowed": false, "preset": 0, "oppTrumpOnly": true, "playDelayPoints": 5, "ABRoom": 0, "ABRoomForever": 0, "leadWrongCardPoints": 10, "followWrongCardPoints": 10, "trumpCallSameSuit": false, "ranks": [{ "rk": "A", "mp": true, "mr": 0, "vr": 0 }, { "rk": "J", "mp": true, "mr": 9, "vr": 5 }], "gameMode": 1, "showQuickTrumpBar": true, "noTrumpNoTurbo": true, "second4Turbo": 15, "winThreadHold": 160, "cardSet": 4, "lastRoundWinScore": 0, "riseRankLimit": 0, "scorePerRank": 80, "ot_plus": 0, "AI": 0, "std": 0, "profile": false, "alertNonMember": true };
        expect(cardRules.followPlayValid(rule, "7", "C", "J", { quadtractor: [], quad: [], tripletractor: [6], triple: [], doubletractor: [], double: [], single: [] }, ["H5", "H5", "H5", "H7", "C4", "C4"], ["H5", "H5", "H5", "JB", "C7", "H7", "C4", "C4", "SA", "ST", "S9", "S9", "DJ", "DJ", "D6"])).to.equal(true);
        expect(cardRules.followPlayValid(rule, "2", "C", "S", { quadtractor: [], quad: [], tripletractor: [], triple: [], doubletractor: [], double: [2], single: [1,1] }, ["S8", "S8", "S7", "S7"], ["SK", "ST", "S8", "S8", "S7", "S7", "S7"])).to.equal(true);
        expect(cardRules.getCardsPattern(rule, 'J', "J", ["DA", "DA", "DA", "DA", "DK", "DK", "DQ", "DQ"]).quad[0]).to.equal(4);
        expect(cardRules.getCardsPattern(rule, 'J', "J", ["DA", "DA", "DA", "DA", "DK", "DK", "DQ", "DQ"]).doubletractor[0]).to.equal(4);
        expect(cardRules.followPlayValid(rule, "J", "J", "D", { quadtractor: [], quad: [4], tripletractor: [], triple: [], doubletractor: [4], double: [], single: [] }, ["D7", "D7", "D4", "D4", "D3", "D3", "D2", "D2"], ["DQ", "D8", "D8", "D7", "D7", "D6", "D4", "D4", "D3", "D3", "D2", "D2"])).to.equal(true);
    });
});
"""

if __name__ == "__main__":
    test()