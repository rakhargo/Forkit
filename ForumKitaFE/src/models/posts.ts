export interface Posts {
    id: string;
    title: string;
    description: string;
    upVote: number;
    downVote: number;
    replies: Replies[];
    creatorId: string;
    subTopiqId: string;
}

export interface Replies {
    reply: string;
    creatorId: string;
}